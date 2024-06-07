
CREATE TABLE <nameofdb>.<nameoftable> (
    home text,
    away text,
    home_win_Probability DOUBLE,
    draw_probability DOUBLE,
    away_win_probability DOUBLE,
    team_to_win_prediction INT,
    average_goals_prediction DOUBLE,
    weather_in_degrees TEXT,
    odds DOUBLE,
    full_time_score TEXT,
    score_at_halftime TEXT,
    date DATETIME,
    time TEXT, --I used time initially but when i push my data into the db it will change to text so might as well just leave it as such
    home_team_score_prediction INT,
    away_team_score_prediction INT,
    home_team_full_time_score INT,
    away_team_full_time_score INT,
    home_team_halftime_score INT,
    away_team_halftime_score INT,
    prediction_result INT,
    day_of_week INT,
    month INT,
    weekly_round INT
);
