-- script that create a mysql index on the table
-- and the firstletter of name and the score
CREATE INDEX idx_name_first_score ON names(LEFT(name, 1), score);