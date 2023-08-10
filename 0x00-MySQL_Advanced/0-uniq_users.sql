-- create table with some attributes
-- should not fail if table exists
CREATE TABLE IF NOT EXISTS users (
    id INT AUTOINCREMENT PRIMARY KEY NOTNULL,
    email VARCHAR(255) NOTNULL UNIQUE,
    name VARCHAR(255)
);