# An-analysis-of-the-EPL

In this project I have tried to use the data of the last 3 seasons of the EPL for EDA regarding the most important stats which help in increasing the position of a team in a season. I have also built a model which predicts the number of goals scored by all the players of the league

### Data Collection
Data was collected from FBref.com.The dataset contains the details of every single player to have played in the Premier League from the 2018-19 season to the 2020-21 season.

There are 8 different tables in our data containing various important stats as follows:
1. Standard Stats: Playing Time (Match Played, Minutes,90’s played), Performance (Goals, Assists,Non-Penalty Goal, etc..), Per 90 Min (Goals/90 mins, Assists/90 mins, Goals & Assists/90 mins,
etc.)
2. Shooting: Standard (Goals, Shots Tot, Shots on Target, Shot Tot/90 min, Shot on Target/90 min,Goals/shot), Expected (Expected Goals, Expected Non- Penalty goals, Goals-Expected Goals), etc.
3. Passing: Total (Passes Completed, Passes Attempted, Pass Completion, Tot Dist, Prog Dist), Short (Passes Completed, Pass Attempted, Passes comp percentages), Medium (Passes Completed, Pass 
Attempted, Passes comp percentages), Long(Passes Completed, Pass Attempted, Passes comp percentages), etc.
4. PassTypes: Live-ball passes, Dead-ball passes, Press pass, Crosses, Corner Kicks(In Swinging Corner Kicks, Out swinging Corner kicks, Straight Corner kicks), Height(Ground passes, Low passes, High passes), Body Part(left leg, right leg, head), etc.
5. Goal and Shot Creation: Shot Creation Action, SCA Types (PassLive, PassDead, Dribbles, Shots), Goal Creation Action(PassLive, PassDead, Dribbles, Shots)
6. Defensive Actions: Tackles (Number of players tackled, tackles in def ⅓, tackles in mid-⅓, tackles in att ⅓), Vs Dribbles(Number of dribbles tackled, Number of times dribbled past plus number of tackles), Pressures, blocks, etc.
7. Possession: Touches (Number of times a player touched the ball, Touches in defensive ⅓, Touches in middle ⅓, Touches in attacking ⅓), Dribbles (Dribbles Completed Successfully, Dribbles Attempted), Target (Number of times a player was the target of an attempted pass, Number of times a player successfully received a pass)
8. Playing Time: Starts (Minutes Per Match Started, Complete matches played), Team Success (PPM -- Points per Match, Goals scored by team while on pitch, Goals allowed by team while on pitch



### Data Scraper
So, the web scraper worked as follows:
1. Went to each Season’s Team Statistics.
2. Each Table has a list of hyperlinks of Team Statistic’s Link encoded in their Team Name.
3. Parse through the hyperlinks for all the available teams
4. Open the page and select the Eight table required to the data we wish to collect by selecting the relevant Table ID. e.g., the Standard statistics table had id stats_shooting_10728.
5. Get the data in the table and concatenate it to the dataset.
6. Save Dataset.

### Data Cleaning
1. Each team’s table contains 2 final values, Squad’s Total and Opponent’s total, which are summarizing attributes. I dropped these in the final dataset.
2. The tables’ columns were multi indexed with most indices being null. Removed this columns
3. The tables that had relevant multi indices were converted as follows: If a table had a collection of columns as “Short Range Passes” with sub columns ‘completed’ ‘attempted’ and ‘total’, the column names were made ‘Short Range Passes_completed’, ‘Short Range_attempted’, ‘Short Range_total’.
4. The table didn’t have the team’s name for each player ,so we added that as one of the attributes.


### EDA: Attributes affecting the team ranking
In my EDA, I wanted to get the attributes which have the most impact on the position increase and decrease of the team in 2018-2019 and 2019-2020 season. We shortlisted 8 team, 4 which had the most positive movement and 4 teams which had the most negative movement in the seasons.
Positive Movement (2018-2019 compared to 2019-2020):
1. Manchester United – 6th to 3rd
2. Leicester City – 9th to 5th
3. Burnley – 15th to 10th
4. Southampton –16th to 11th

Negative Movement (2018-2019 compared to 2019-2020)
1. Everton – 8th to 12th
2. West Ham United –- 10th to 16th
3. Watford –- 11th to 19th
4. Bournemouth –- 14th to 18th

Here are some of the attributes that showed the most variation among the selected teams:
1. Goal Creation Actions - Field.
2. Passing Success Percentage
3. Mid-3rd Passing- Successful
4. Tackles that won possession of the ball
5. Defensive tackles in 1/3rd.
6. Interceptions



### Model: Finding the attributes and predicting goals hit by a player in the EPL
The attributes that affect the number of goals scored by a player are found by performing PCA on the subset of players that play in forward position as they are the ones that score more goals, and their attributes are more relevant for the prediction of number of goals scored.

K-Means clustered the players of similar quality. To make sense of the clusters, I used the cluster labels to make a decision tree to see how the attributes are used in clustering of the players into a player cluster. After I got the data, I had to train a model using the attributes from the decision tree to predict the number of goals that the player can score in the next season. This means that we need to build a regression model. As a baseline, I trained a decision tree regressor. The model was trained on the 2019-19 and 2019-2020 season and our goal was to correctly predict the goals for the 2020-2021. I saw the feature which contributed most to the decision tree regressor.


### Libraries Used
pandas

seaborn

numpy

matplotlib

sklearn

BeautifulSoup

requests