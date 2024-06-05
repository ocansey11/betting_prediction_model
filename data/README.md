# Data

This directory contains the datasets scraped, cleaned, and prepared for the betting prediction model. The datasets are stored in CSV format for easy access and analysis.

## Files:

- **training_data.csv**: Dataset containing features and outcomes of completed matches used for training the prediction model.
- **testing_data.csv**: Dataset containing features of upcoming matches used for testing the prediction model.
- **completed_matches.csv**: Dataset containing historical data of completed matches per week, including match statistics before the games were played and predicted outcomes vs results .
- **upcoming_matches.csv**: Dataset containing information about upcoming matches, including match details and predictions.
- **previous_week_league_standings.csv**: Dataset containing the Premier League standings before the matches are played but attached to the completed_matches data with the results of those matches. I usually scrape and clean this the day before the weekly round
- **current_week_league_standings.csv**: Dataset containing the Premier League standings before upcoming matches are played in the current week but attached to upcoming matches.

## Automation for Database Integration:

- The CSV data in this directory can be easily integrated into a database using the provided automation scripts withing the directory. These scripts fetch the CSV data and insert it into the database tables, allowing seamless access to the data for further analysis or model training.

## Usage:

- **Training and Testing Data**: `training_data.csv` and `testing_data.csv` are the primary datasets used for training and evaluating the prediction
- The training data will be split into train and test data
- The testing_data will be purely for evaluatin the models performance on new unseen data (unfortunately there are duplicates here)

## Notes:

The datasets are cleaned and formatted to ensure consistency and ease of analysis. However, some preprocessing may be required based on specific analysis or modeling requirements. example are encoding team labels as integers and mapping them.
Also encoding team to win prediction. Numbers are easier to handle while training models

The dictionary below provides info of these figures.

#### These team_labels match all the data from the other notebooks

team_labels = {

-     'Arsenal': 1,
-     'Aston Villa': 2,
-     'Bournemouth': 3,
-     'Brighton': 4,
-     'Burnley': 5,
-     'Chelsea': 6,
-     'Crystal Palace': 7,
-     'Everton': 8,
-     'Fulham': 9,
-     'Leeds Utd': 10,
-     'Leicester City': 11,
-     'Liverpool': 12,
-     'Man City': 13,
-     'Man Utd': 14,
-     'Newcastle': 15,
-     'Norwich': 16,
-     'Sheffield': 17,
-     'Southampton': 18,
-     'Tottenham': 19,
-     'West Ham': 20,
-     'Luton': 21,
-     'Wolves': 22,
-     'Brentford': 23,
-     'Sheffield Utd': 24,
-     'Forest': 25

  }

  Label Mapping for `team_to_win_prediction` column : {'1': 0, '2': 1, 'X': 2} where

  - 0 means home team to win
  - 1 means away team to win and
  - 2 means draw

  However when i finally validate the data in my models and print the results of my models predictions i switch the labels to for easy reading
