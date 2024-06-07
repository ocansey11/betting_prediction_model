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

Unfortunately, the tables do not come with any data. Hence the following sql scripts
`testing_data_automation.sql`
`training_data_automation.sql`
might run into a few errors.

Data
You can import and insert csv data from `data` folder into these tables after creation before you run the `automation` sql scripts


