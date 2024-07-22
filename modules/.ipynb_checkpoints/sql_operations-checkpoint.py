from sqlalchemy import text
def execute_sql(engine, sql_script):
    """
    Execute the provided SQL script.
    """
    with engine.connect() as connection:
        connection.execute(text(sql_script))

        
# These scripts are for merging pairs of data. However over time, i will have csv files from these processes. Hence Training and testing data will be appended by just downloading and importing these csv files. 

CREATE_COMPLETED_MATCHES_TABLE = """ 
CREATE TABLE IF NOT EXISTS completed_matches (
    home TEXT,
    away TEXT,
    home_win_probability DOUBLE,
    draw_probability DOUBLE,
    away_win_probability DOUBLE,
    team_to_win_prediction INT,
    average_goals_prediction DOUBLE,
    weather_in_degrees TEXT,
    odds DOUBLE,
    full_time_score TEXT,
    score_at_halftime TEXT,
    date DATETIME,
    time TEXT,
    home_team_score_prediction INT,
    away_team_score_prediction INT,
    home_team_full_time_score INT,
    away_team_full_time_score INT,
    home_team_halftime_score INT,
    away_team_halftime_score INT,
    prediction_result TEXT,
    day_of_week INT,
    month INT,
    weekly_round BIGINT
);
"""

CREATE_UPCOMING_MATCHES_TABLE = """
CREATE TABLE IF NOT EXISTS upcoming_matches (
    home INT,
    away INT,
    home_win_probability DOUBLE,
    draw_probability DOUBLE,
    away_win_probability DOUBLE,
    team_to_win_prediction INT,
    scoreline_prediction TEXT,
    average_goals_prediction DOUBLE,
    weather_in_degrees TEXT,
    odds DOUBLE,
    date DATETIME,
    time TIME,
    home_team_score_prediction INT,
    away_team_score_prediction INT,
    day_of_week INT,
    month INT,
    weekly_round INT
);
"""

CREATE_PREVIOUS_WEEK_STANDINGS_TABLE = """
CREATE TABLE IF NOT EXISTS previous_week_league_standings (
    Pos INT,
    Team INT,
    Pld INT,
    Wins INT,
    Draws INT,
    Losses INT,
    GF INT,
    GA INT,
    Ppg_Last_5_Matches DOUBLE,
    Points INT
);
"""

CREATE_CURRENT_WEEK_STANDINGS_TABLE = """
CREATE TABLE IF NOT EXISTS current_week_league_standings (
    Pos INT,
    Team INT,
    Pld INT,
    Wins INT,
    Draws INT,
    Losses INT,
    GF INT,
    GA INT,
    Ppg_Last_5_Matches DOUBLE,
    Points INT
);
"""


CREATE_TRAINING_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS training_data AS
SELECT 
	cm.*,
    home_team.Pos AS home_team_pos,
    home_team.Pld AS home_team_matches_played,
    home_team.Wins AS home_team_wins,
    home_team.Draws AS home_team_draws,
    home_team.Losses AS home_team_losses,
    home_team.GF AS home_team_gf,
    home_team.GA AS home_team_ga,
    home_team.Ppg_Last_5_Matches AS home_team_ppg_last_5_matches,
    home_team.Points AS home_team_points,
    away_team.Pos AS away_team_pos,
    away_team.Pld AS away_team_matches_played,
    away_team.Wins AS away_team_wins,
    away_team.Draws AS away_team_draws,
    away_team.Losses AS away_team_losses,
    away_team.GF AS away_team_gf,
    away_team.GA AS away_team_ga,
    away_team.Ppg_Last_5_Matches AS away_team_ppg_last_5_matches,
    away_team.Points AS away_team_points
FROM 
    completed_matches cm
INNER JOIN 
    previous_week_league_standings home_team ON cm.Home = home_team.Team
INNER JOIN 
    previous_week_league_standings away_team ON cm.Away = away_team.Team;
"""



CREATE_TESTING_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS testing_data AS
SELECT 
	um.*,
    home_team.Pos AS home_team_pos,
    home_team.Pld AS home_team_matches_played,
    home_team.Wins AS home_team_wins,
    home_team.Draws AS home_team_draws,
    home_team.Losses AS home_team_losses,
    home_team.GF AS home_team_gf,
    home_team.GA AS home_team_ga,
    home_team.Ppg_Last_5_Matches AS home_team_ppg_last_5_matches,
    home_team.Points AS home_team_points,
    away_team.Pos AS away_team_pos,
    away_team.Pld AS away_team_matches_played,
    away_team.Wins AS away_team_wins,
    away_team.Draws AS away_team_draws,
    away_team.Losses AS away_team_losses,
    away_team.GF AS away_team_gf,
    away_team.GA AS away_team_ga,
    away_team.Ppg_Last_5_Matches AS away_team_ppg_last_5_matches,
    away_team.Points AS away_team_points
FROM 
    upcoming_matches um
INNER JOIN 
    current_week_league_standings home_team ON um.Home = home_team.Team
INNER JOIN 
    current_week_league_standings away_team ON um.Away = away_team.Team;
    
"""



# SQL CODES DROPPING THE VIEWS
DROP_VIEW_COMBINED_TRAIN_DATA = """
DROP VIEW IF EXISTS combined_train_data;
"""

DROP_VIEW_COMBINED_TEST_DATA = """
DROP VIEW IF EXISTS combined_test_data;
"""



# SQL CODES CREATING THE VIEWS
CREATE_VIEW_TRAIN_DATA = """
CREATE VIEW combined_train_data AS
SELECT 
    cm.*,
    home_team.Pos AS home_team_pos,
    home_team.Pld AS home_team_matches_played,
    home_team.Wins AS home_team_wins,
    home_team.Draws AS home_team_draws,
    home_team.Losses AS home_team_losses,
    home_team.GF AS home_team_gf,
    home_team.GA AS home_team_ga,
    home_team.Ppg_Last_5_Matches AS home_team_ppg_last_5_matches,
    home_team.Points AS home_team_points,
    away_team.Pos AS away_team_pos,
    away_team.Pld AS away_team_matches_played,
    away_team.Wins AS away_team_wins,
    away_team.Draws AS away_team_draws,
    away_team.Losses AS away_team_losses,
    away_team.GF AS away_team_gf,
    away_team.GA AS away_team_ga,
    away_team.Ppg_Last_5_Matches AS away_team_ppg_last_5_matches,
    away_team.Points AS away_team_points
FROM 
    completed_matches cm
INNER JOIN 
    previous_week_league_standings home_team ON cm.Home = home_team.Team
INNER JOIN 
    previous_week_league_standings away_team ON cm.Away = away_team.Team;


"""

CREATE_VIEW_TEST_DATA  = """
CREATE VIEW combined_test_data AS
SELECT 
	um.*,
    home_team.Pos AS home_team_pos,
    home_team.Pld AS home_team_matches_played,
    home_team.Wins AS home_team_wins,
    home_team.Draws AS home_team_draws,
    home_team.Losses AS home_team_losses,
    home_team.GF AS home_team_gf,
    home_team.GA AS home_team_ga,
    home_team.Ppg_Last_5_Matches AS home_team_ppg_last_5_matches,
    home_team.Points AS home_team_points,
    away_team.Pos AS away_team_pos,
    away_team.Pld AS away_team_matches_played,
    away_team.Wins AS awaycurrent_week_league_standings_team_wins,
    away_team.Draws AS away_team_draws,
    away_team.Losses AS away_team_losses,
    away_team.GF AS away_team_gf,
    away_team.GA AS away_team_ga,
    away_team.Ppg_Last_5_Matches AS away_team_ppg_last_5_matches,
    away_team.Points AS away_team_points
FROM 
    upcoming_matches um
INNER JOIN 
    current_week_league_standings home_team ON um.Home = home_team.Team
INNER JOIN 
    current_week_league_standings away_team ON um.Away = away_team.Team;

"""

# SQL CODES INSERTING NEW DATA THROUGH VIEWS
INSERT_VIEW_TRAIN_DATA = """ 
INSERT INTO training_data SELECT * FROM combined_train_data;
"""


INSERT_VIEW_TEST_DATA = """ 
INSERT INTO testing_data SELECT * FROM combined_test_data;
"""

# -- CREATE EVENT append_training_data
# -- ON SCHEDULE EVERY 1 WEEK
# -- DO
# -- INSERT INTO training_data
# -- SELECT * FROM combined_train_data;


# -- CREATE EVENT append_testing_data
# -- ON SCHEDULE EVERY 1 WEEK
# -- DO
# -- INSERT INTO testing_data
# -- SELECT * FROM combined_test_data;



# FOR USER WHO ARE COPYING THE ALREADY ACCUMULATED TRAINING AND TESTING DATA FOR DATA ANALYSIS OR ANY OTHER PURPOSES USE THE FOLLOWING OPERATIONS
# THE IDEA IS TO CREATE A TRAINING AND TESTING DATA TABLE IN YOUR DB.
# COPY THE CSV DATA FOR BOTH TESTING AND TRAINING DATA FROM  THE csv DIRECTORY IN THE MAIN BRANCH - I WILL BE UPDATING THESE CSVS' WEEKLY 
# INSERT THE training_data and testing_data CSV data  INTO THE VARIOUS TABLE TO GET A JUMP START TO TRAIN YOUR MODELS OR DO YOUR ANALYSIS

CREATE_TABLE_TRAINING_DATA_FOR_CSV_INSERTION =  """
CREATE TABLE training_data (
    home INT,
    away INT,
    home_win_probability DOUBLE,
    draw_probability DOUBLE,
    away_win_probability DOUBLE,
    team_to_win_prediction INT,
    average_goals_prediction DOUBLE,
    weather_in_degrees TEXT,
    odds DOUBLE,
    full_time_score TEXT,
    score_at_halftime TEXT,
    date DATETIME,
    time TIME,
    home_team_score_prediction INT,
    away_team_score_prediction INT,
    home_team_full_time_score INT,
    away_team_full_time_score INT,
    home_team_halftime_score INT,
    away_team_halftime_score INT,
    prediction_result INT,
    day_of_week INT,
    month INT,
    weekly_round INT,
    home_team_pos INT,
    home_team_matches_played INT,
    home_team_wins INT,
    home_team_draws INT,
    home_team_losses INT,
    home_team_gf INT,
    home_team_ga INT,
    home_team_ppg_last_5_matches DOUBLE,
    home_team_points INT,
    away_team_pos INT,
    away_team_matches_played INT,
    away_team_wins INT,
    away_team_draws INT,
    away_team_losses INT,
    away_team_gf INT,
    away_team_ga INT,
    away_team_ppg_last_5_matches DOUBLE,
    away_team_points INT
);
"""


CREATE_TABLE_TESTING_DATA_FOR_CSV_INSERTION =  """
CREATE TABLE testing_data (
    home INT,
    away INT,
    home_win_probability DOUBLE,
    draw_probability DOUBLE,
    away_win_probability DOUBLE,
    team_to_win_prediction INT,
    scoreline_prediction TEXT,
    average_goals_prediction DOUBLE,
    weather_in_degrees TEXT,
    odds DOUBLE,
    date DATETIME,
    time TIME,
    home_team_score_prediction INT,
    away_team_score_prediction INT,
    day_of_week INT,
    month INT,
    weekly_round INT,
    home_team_pos INT,
    home_team_matches_played INT,
    home_team_wins INT,
    home_team_draws INT,
    home_team_losses INT,
    home_team_gf INT,
    home_team_ga INT,
    home_team_ppg_last_5_matches DOUBLE,
    home_team_points INT,
    away_team_pos INT,
    away_team_matches_played INT,
    away_team_wins INT,
    away_team_draws INT,
    away_team_losses INT,
    away_team_gf INT,
    away_team_ga INT,
    away_team_ppg_last_5_matches DOUBLE,
    away_team_points INT
);

"""