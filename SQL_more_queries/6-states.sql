-- Creates the database `hbtn_0d_usa` and the table `states`

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create table `states` if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
