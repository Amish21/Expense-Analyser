# Expense Analyzer (Python + MySQL)

A command-line expense tracking application built using Python and MySQL.
The application stores expenses in a relational database and provides
both summary views (total and category-wise spending) and a detailed
ledger view of all recorded transactions.

This project demonstrates backend fundamentals such as database
connectivity, SQL aggregation, and menu-driven CLI application design.

---

## Features

- Add expenses with date, amount, category, and description
- View total expenses stored in the database
- View expenses grouped by category using SQL aggregation
- View all recorded expenses in a ledger-style format (with dates)
- Clear all stored expenses
- Persistent data storage using MySQL

---

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python

---

## Database Schema

```sql
CREATE DATABASE expense_db;
USE expense_db;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);
```
---

## Project Structure

```text
expense-analyzer/
├── src/
│   └── analyzer.py
├── sql/
│   └── schema.sql
├── README.md
├── requirements.txt
└── .gitignore
```
---

## How To Run:
1.) Install Python 3 and MySQL
2.) Install required dependency:
pip install mysql-connector-python
3.) Create the database and table using the schema above
4.) Update database credentials in the source code if needed:
host="localhost"
port=3306
user="root"
password="YOUR_PASSWORD"
database="expense_db"
5.) Run the application:
python src/analyzer.py

---

## Cli Output

```text
1. Add Expense
2. Show total expense
3. Show expense by category
4. Show all expenses
5. Clear all expenses
6. Exit
Choose an option --> 4

All expenses:
xxxxxxxxxxxxxxxxx
Date     | Category      | Amount       | Description
xxxxxxxxxxxxxxxxx
2026-01-13 | utilities    | 2500.00 | rent
```
---

## Config Notes
1.) The default MySQL port (3306) is used

2.) Database connection details (host, port, username, password)
can be modified to match the local MySQL setup

3.) The application uses a persistent database; data remains available
between program runs unless explicitly cleared

---

## Learning Outcome 
1.) Connecting Python applications to relational databases

2.) Writing SQL queries with aggregation (SUM, GROUP BY)

3.) Designing menu-driven CLI applications

4.) Working with persistent data storage

5.) Debugging real-world runtime and logic issues

---

## License 
This project is intended for learning and personal use.
