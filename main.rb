require_relative 'controllers/data_controller.rb'
require 'pry'
require 'csv'

return unless ARGV.length == 1

client = DataController.new
from = "assets/#{ARGV[0]}"
to = "assets/game_log.csv"
client.add_headers(to) unless client.csv_has_headers?(to)

CSV.foreach(from, headers: true) do |row|
  result = client.get_pitcher_data(row["id"])
  game_logs = client.filter_pitcher_data_by_games(result, row)
  client.export_data(to, game_logs, append = true)
end