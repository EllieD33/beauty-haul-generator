DROP DATABASE IF EXISTS beauty_haul_generator;
CREATE DATABASE beauty_haul_generator;
USE beauty_haul_generator;


CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL
    );


INSERT INTO users (username) VALUES ('guest');


CREATE TABLE user_routines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE routine_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    routine_id INT,
    brand VARCHAR(100),
    product VARCHAR(255),
    price DECIMAL(10,2),
    product_desc TEXT,
    score INT,
    FOREIGN KEY (routine_id) REFERENCES user_routines(id)
);
