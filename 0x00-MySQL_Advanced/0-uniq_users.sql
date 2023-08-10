-- create table with some attributes
-- should not fail if table exists
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTOINCREMENT PRIMARY KEY NOTNULL,
    email VARCHAR(255) NOTNULL UNIQUE,
    name VARCHAR(255)
);