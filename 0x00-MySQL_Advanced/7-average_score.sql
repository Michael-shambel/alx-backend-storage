-- script that creates a view need_meeting that list all students that hav a score
-- under 80 (strict) and no last_meeting and more than one month

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score INT;
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;
    UPDATE users
    SET users.average_score = avg_score
    WHERE users.id = user_id;
END $$

DELIMITER ;
