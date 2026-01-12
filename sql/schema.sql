CREATE DATABASE expense_db;
USE expense_db;
create table if not exists transactions(
id INT AUTO_INCREMENT PRIMARY KEY,
date DATE NOT NULL,
amount decimal(10,2) NOT NULL,
category varchar(100) NOT NULL,
description varchar(255)
);