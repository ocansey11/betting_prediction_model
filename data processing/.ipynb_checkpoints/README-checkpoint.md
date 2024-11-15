# Data Preprocessing

This part of the project involves preprocessing the scraped data to create training and testing datasets for the betting prediction model. The process involves running several Jupyter notebooks to scrape data from various sources and combine them into cohesive datasets.

## Requirements
- Understand the flowchart and the `timing` of having respective data such as previous_league_standings and current_leagues standings.
- Go to data scraping folder. Run the respective notebooks in their respective order. Note: some notebooks need to be run a day before upcoming matches are played(`Scrapping Premier League Table (For Training).ipynb`). Then another to be run after matches are played(`Scrapping Forebet Prediction Table Completed Matches.ipynb`). This makes up yur training data.
-  `Betting Prediction Model- Scraping Premier League Table (For Testing).ipynb` & `Betting Prediction Model - Scrapping Forebet Upcoming Matches.ipynb` combine to give you your testing data and can be run at the same time.
- Have `completed_matches`, `upcoming_matches`, `previous_league_standings`, `current_league_standings` ready

### Reminder of scrapping Data Notebooks
The following Jupyter notebooks are used to scrape data:
- `Betting Prediction Model - Scrapping Forebet Prediction Table Completed Matches.ipynb`: Scrapes data for completed matches from the Forebet prediction table.
- `Betting Prediction Model - Scrapping Forebet Upcoming Matches.ipynb`: Scrapes data for upcoming matches from the Forebet prediction table.
- `Betting Prediction Model - Scrapping Premier League Table (For Training).ipynb`: Scrapes data for the Premier League table, used for training the model.
- `Betting Prediction Model- Scraping Premier League Table (For Testing).ipynb`: Scrapes data for the Premier League table, used for testing the model.

## Combining Data Notebooks

After scraping the necessary data, the following Jupyter notebooks are used to combine the data into training and testing datasets:

- `Creating all Tables Option 1` : Creates all required tables prior to combining/merging.
- `Creating all Tables Option 2`: Creates the training and testing tables prior to inserting data into these tables from `../data/training.csv and ../data/testing.csv` 
- `Combining Tables for training_data.ipynb`: Combines the scraped data into the training dataset. (`completed_matches` & `previous_week_league_standings`) Make sure they are in your db or you might run into errors
- `Combining Tables for testing_data.ipynb`: Combines the scraped data into the testing dataset. (`upcoming_matches` & `current_week_league_standings`)
- 

## Summary
   ### Option 1
1. **Scraping Data**: Run the scraping notebooks to collect data from the specified sources.
2. **Combining Data**: After scraping, run the combining notebooks to merge the scraped data into training and testing datasets.

   ### Option 2
1. **Create Training & Testing Data** Just run the script in Option 2. This replaces your train and test data with the weekly updated csv files.  

#### Important Notes - Option 1
- Make sure to run the scraping notebooks before attempting to combine the data.
- The combined datasets should be saved in a format suitable for model training and evaluation.

## Contributing

Contributions to the data preprocessing notebooks are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
