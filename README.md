# Betting Prediction Model

This project aims to predict football match outcomes using data scraped from various sources (Forebet.com and Sofascore). The project includes data scraping, processing, exploratory data analysis, model training, and evaluation.

## Project Structure

### Data

- **data/csv/**: Contains the weekly accumulated and updated training(completed_match + previous league stats) and testing datasets(upcoming_matches + current league stats).

### Notebooks found in various directories

- **notebooks/data_scraping/**: Notebooks for scraping completed matches, upcoming matches, and league table standings.
- **notebooks/data_processing/**: Notebooks for combining the scraped data into training and testing datasets.
- **notebook/exploratory_data_analysis.ipynb**: Notebook for exploring the data. finding interesting patterns as the data grows weekly
- **notebook/model_classifiers.ipynb**: Notebook for training and comparing different classifiers. The top three classifiers from this notebook will be expanded on. As the data grows new classifiers might perform better than old ones.
- **notebooks/models**: Notebooks for tuning the best models and testing them out.

### SQL Scripts

- **sql_scripts/**: SQL scripts for creating tables and inserting data. incase you want to try and edit somethings on your own

### Source Code

- **modules/**: Python modules for database connections and SQL operations.

### Flowcharts

- **flowcharts/**: Diagrams explaining the data flow and processing steps.

## How to Use

### Option 1: Follow the Full Process

1. **Scrape Data**: Use the notebooks in `betting_prediction_model/data_scraping/` to scrape the latest data hence creating and storing them in a db
2. **Process Data**: Use the notebooks in `betting_prediction_model/data_processing/` to combine the scraped data into training and testing datasets.
3. **Train Models**: Use `betting_prediction_model/comparing_classifiers.ipynb` to train and compare different models. and pick which one fits best. Currently we have little data. When the next season starts we will have really good data to work on
4. **Tune Models**: Use `betting_prediction_model/models` to tune the best models individual. This helps you focus on your favorite model and play around with parameters and hyperparameters to yeild the best results

### Option 2: Use Pre-Processed Data

1. **Download Data**: Download the weekly accumulated and updated training and testing datasets from `betting_prediction_model/data`.
2. **Train Models**: Use `betting_prediction_model/comparing_classifiers.ipynb` to train and compare different models using the downloaded datasets.
3. **Tune Models**: Use `betting_prediction_model/models.ipynb` to tune the best models.

## Requirements

ChromeDriver
My sql Workbench
Python 3.0+
