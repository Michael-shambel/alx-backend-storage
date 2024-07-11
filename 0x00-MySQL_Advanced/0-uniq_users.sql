-- script that creates a table user that contain differnt column
-- the database name is called holberton
CREATE DATABASE IF NOT EXISTS holberton;

USE holberton;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
