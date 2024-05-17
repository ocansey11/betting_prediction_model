
drop table bet_prediction_model.forebet_prediction_table;

CREATE TABLE bet_prediction_model.forebet_prediction_table (
    Home INT,
    Away INT,
    Home_Win_Probability DOUBLE,
    Draw_Probability DOUBLE,
    Away_Team_Win_Probability DOUBLE,
    Team_To_Win_Prediction INT,
    Average_Goals_Prediction DOUBLE,
    Weather_In_Degrees TEXT,
    Odds DOUBLE,
    Full_Time_Score TEXT,
    Score_At_Halftime TEXT,
    Date DATETIME,
    Time TIME,
    Home_Team_Score_Prediction INT,
    Away_Team_Score_Prediction INT,
    Home_Team_Full_Time_Score INT,
    Away_Team_Full_Time_Score INT,
    Home_Team_Halftime_Score INT,
    Away_Team_Halftime_Score INT,
    Prediction_Result_Won_Loss INT,
    Day_Of_Week INT,
    Month INT,
    Weekly_Round INT
);
INSERT INTO bet_prediction_model.forebet_prediction_table
SELECT * FROM sandbox.forebet_prediction_table;


