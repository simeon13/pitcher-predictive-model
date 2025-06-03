## Pitching Predictive Model

### What does this model predict?
* *This model predicts how many strikeouts a given starting pitcher will have against a specific on a specific day.*

### What is this model based on?
* *This model learns patterns using historical box scores and contextual game features available before each game.*
* *This includes average recent strikeouts,average season strikeouts, days of rest, and opponent strikeout tendencies (including throwing hand).*
* *It also uses a mix of player performance, opponent behavior, and game context to predict the number of strikeouts a pitcher will get in a given game.*

### What is the model type?
* *This model is a Random Forest Regressor -- A tree-based ensemble method that learns patterns from historical data to predict a continuous value (strikeouts).*

### What data is used to train the model?
* *Game logs are grabbed for almost all starting pitchers in the MLB via the ESPN API to provide accurate information for this model to learn from.*

### How accurate is this model?
* *This model was only recently created so it's effectiveness is still being studied. More information will be provided later to provide it's accuracy.*
* *As time goes on, this model should only become more accurate with more data (games played).*

### What flaws could affect this model?
* *In the MLB, there are sometimes starters that are injured or sent to the minor leagues. THis means some games are entirely used and can affect the model.*
* *In addition, this model doesn't fully account for injuries on a team right away. For example, if a batter on a team suffers a major injury,
  it could take a few games for the model to see a trend on the opposing team if there is one.*

