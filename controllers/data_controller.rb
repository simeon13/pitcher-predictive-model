require 'httparty'
require 'json'
require 'date'
require 'csv'

class DataController
    include HTTParty
    
    def get_pitcher_data(id)
        endpoint = "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/athletes/#{id}/gamelog"
        response = self.class.get(endpoint)

        if response.success?
            JSON.parse(response.body)
        else
            raise "Error fetching data: #{response.code}"
        end
    end
    
    def filter_pitcher_data_by_games(data, row)
        game_log = []
        teams = data["events"].map { |event| event.last["opponent"]["abbreviation"] }
        dates = data["events"].map { |event| Date.parse(event.last["gameDate"]).to_s }
      
        data["seasonTypes"].first["categories"].each do |month|            
            month["events"].each do |event|
                stats = event["stats"]
                ## team, hand, date, walks, pitches, battersFaced, and strikeouts to predict strikeouts for next game
                game_log << [row["name"], row["hand"], teams.shift, dates.shift, stats[5], stats[9], stats[10], stats[6]]
            end
        end
        
        return game_log
    end
    
    def add_headers(path)
        CSV.open(path, "w") do |csv|
            csv << ["player", "hand", "opponent", "date", "walks", "pitches", "battersFaced", "strikeouts"]
        end
    end
    
    def export_data(path, data, append)
        mode = append ? "a" : "w"
        CSV.open(path, mode) do |csv|
            data.each { |row| csv << row }
        end
    end
    
    def csv_has_headers?(path)
        first_row = nil
        CSV.open(path, 'r') do |csv|
            first_row = csv.first
        end

        # Heuristic check: are all elements strings and not numbers? 
        # This is simple and might need to be adapted depending on your data
        first_row&.all? { |cell| cell =~ /\D/ }  # true if all cells have at least one non-digit char
    end
end
