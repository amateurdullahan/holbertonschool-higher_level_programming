-- What does Webster say about soul?
-- All I want is a good home and a wife
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'htbn_0d_usa'.'cities'(
       id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES 'hbtn_0d_usa'.'states'(id)
);
