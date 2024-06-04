## First time users:

Hey guys, to get a better understanding of this project i will suggest downloading the flowchart and opening it in draw.io.
The project is simple, i am scraping data (completed_matches and upcoming matches) from forebet.com as well as the league standings in this case the `English Premier League` to train my various models and then test them out.

- The training data will consist of a combination of `completed_matches` and the previous league standings.(the stats before the matches `were` played)
- The test data will consist of the a combination of the `upcoming_matches` and the current league standings.(the stats before the matches `are` played)
- For this project i am using python version 3.0+ and Mysql Workbench

### Running Notebooks in Order

At the beginning of the project make sure you run the notebooks in the following order

1. Betting Prediction Model - Scraping Premier League Table (For Training) - Since the upcoming matches will soon become `completed_matches` we want to get the current league standings before the matches are played. The standings will be put in `previous_week_league_standings`. After the matches are played we will run the notebook to scrape the now `completed_matches`. Hence run this notebook a day before the matches have been played

2. Betting Prediction Model - Scrapping Forebet Prediction Table Completed Matches - After the matches have been played, we scrap this data to combine with the `previous_week_league_standings`. This becomes our `training_data`

3. Betting Prediction Model - Scrapping Premier League Table (For Testing) - Since we want to test the model on upcoming matches will scrape the current league standings in order to combine that data with upcoming matchings

4. Betting Prediction Model - Scrapping Forebet Prediction Table Upcoming Matches - The matches yet to played will test how accurate our model is, we scrape this data and store in our database as `upcoming_matches` to combine with the `current_week_league_standings`. This becomes our `testing_data`

5. Combining Tables and executing Scripts - I have scripts in SQL Scripts directory for you to hard code some data and test the model out yourself. or you can run this code once you have your `completed_matches`, `previous_week_league_standings`,`current_week_league_standings`, `upcoming_matches`.

6. Betting Prediction Model - Comparing Classifiers - Run this notebook to pick the best Classification Model. This is a very important notebook. with few data, i had to resample to cater for imbalance, but as the data grows, always come back to this to see which model is getting better, and which model isnt. It will also show patterns in models. for examples when the forebet websites says theres alot of draws this week some models might be better at sniffing out past predictions similar to future predictions done some. I would have love to elaborate more on this. its tricky to explain.

7. Betting Prediction Model - Model. Currently i am playing around with Logistic regression. I will update the project and add a couple other notebooks for various other models. these will consists of tunings and other processes like resample scaling etc. These will vary per the model in order to make them better. Stay tuned

## Experienced Users

1. **Scrapping Premier League Table for Training Data:** Before running 'Betting Prediction Model - Scrapping Forebet Completed Matches', ensure to scrape the Premier League table for training data the days before you scrape "completed matches. This step provides the previous league standing stats before the upcoming matches are played.

2. **Completed Matches Data:** This data will be joined with the `previous_week_league_standings` table in your database to prepare the model.

3. **Data Accumulation:** After the week has passed and you have your completed matches and previous league standings ready in your database, follow this pattern:

   - Join the completed matches with the previous league standings and append the result to `training_data`.
   - Train your model and test it by running 'Betting Predictions Model - Model'.(be it logistic, rbf random forest. i will create different notebooks for various notebooks)
   - As the data grows the main question will be are the model getting better or worse?

### Test Data

1. **Upcoming Matches Data:** Similar to the process for training data, scrape the Premier League table for upcoming matches and join it with the current league standings. Unlike training data, this process can be done on the same day to test the model with current data.

   - Join the upcoming matches with the current league standings and append the result to `testing_data`.
   - Test your model's predictions by running 'Betting Predictions Model - Model' with the testing data. after you have trained and fitted the model ofcourse.
   - You can take a look at the logistic regression notebook to have a fair idea of how the columns for training and testing data must match. even after you have trained and tuned your model by lets say reducing parameters you have to do the same for the testing data.

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
-     'Liverpool':12,
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

Label Mapping for team_to_win_prediction : {'1': 0, '2': 1, 'X': 2}
where 0 means home team to win
1 means away team to win and
2 means

## Model Prediction Results Caveat:

When appending the results of model predictions to the upcoming matches data, users can remap the `team_labels` and `team_to_win_prediction` labels by switching the keys and values. For example:

If team labels were initially {Arsenal:1} , if you want to remap you have to change the labels to {1:Arsenal}. and then remap to the dataframe. Similarly, in the label mapping for team to win prediction, the keys and values can be switched to better intepret the data the model is referring to...

- You can see a glimpse of this in `Betting tip Models/models/Betting Prediction Model- Logistic Regression.ipynb` notebook

## Disclaimer:

The predictions generated by this project are based on statistical analysis and machine learning algorithms. While every effort has been made to ensure the accuracy of the predictions, they should be used for informational purposes only. We do not guarantee the accuracy or reliability of the predictions, and we are not liable for any losses or damages resulting from the use of the predictions for betting or any other purposes.

Attribution:
Data for completed and upcoming matches is sourced from Forebet
League standings data is obtained from various sources but mainly SofaScore.
