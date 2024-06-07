# SQL Scripts

This directory contains SQL scripts used for database operations in the project.

## Description

In case you encounter any issues with the automation scripts provided, or if you need to recreate the tables manually for any reason, you can use these SQL scripts to create the necessary tables in your MySQL database.

## Usage

To create the tables manually using these SQL scripts, follow these steps:

1. Connect to your MySQL database using a tool such as MySQL Workbench or through your preferred MySQL client.
2. Chose the db you want to store all the tables
3. Open the SQL script file for example (`completed_matches.sql`) in your MySQL client.
4. Execute the SQL script to create the tables in your database.

Unfortunately, the scripts do not insert any data into the tables. Hence the following sql scripts
`testing_data_automation.sql`
`training_data_automation.sql`
might run into a few errors because they rely on a combination of paired tables.

### Note:
So after creating the tables, you need to import data into `completed_matches`, `upcoming_matches`, `previous_league_standings`, `current_league_standings` before you can run `testing_data_automation.sql`, and `training_data_automation.sql`

## Data
You can import and insert csv data from `data` folder into these tables( `completed_matches`, `upcoming_matches`, `previous_league_standings`, `current_league_standings`) after creation `before` you run the `automation` sql scripts for training and testing.

## Steps for importing

### Prepare Your CSV Data
Ensure your CSV data files are ready and located in the data folder
Files include completed_matches.csv, upcoming_matches.csv, previous_league_standings.csv, and current_league_standings.csv.

### Import CSV Data into Tables
Go to the Schema section and select your database.
Right-click on the table where you want to import data (e.g., completed_matches) and select Table Data Import Wizard.


### Using the Table Data Import Wizard
Click Next on the welcome screen of the wizard.
Browse to select your CSV file (e.g., completed_matches.csv) and click Next.
Verify the data preview and click Next.
Map the CSV columns to the table columns. Ensure each CSV column is correctly mapped to the corresponding table column.
Click Next and then Next again to import the data.
Click Finish to complete the import process.

### Repeat for Each Table
Repeat the above steps to import data for the other tables (upcoming_matches, previous_league_standings, current_league_standings) using their respective CSV files.


