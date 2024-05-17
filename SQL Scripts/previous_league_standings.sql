CREATE TABLE `bet_prediction_model`.`previous_week_league_standings` (
    `Pos` INT,                      -- Position in the league table
    `Team` INT,                  -- Team label
    `Pld` INT,                      -- Matches played
    `Wins` INT,                     -- Number of wins
    `Draws` INT,                    -- Number of draws
    `Losses` INT,                   -- Number of losses
    `GF` INT,                       -- Goals for
    `GA` INT,                       -- Goals against
    `Ppg_Last_5_Matches` DOUBLE,   -- Last 5 matches result (e.g., 'WDLWL') Points per game              
    `Points` INT                    -- Total points
);