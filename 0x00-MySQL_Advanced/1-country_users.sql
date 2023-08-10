-- In or not out
CREATE TABLE IF NOT EXISTS users (
    id INT NOTNULL AUTOINCREMENT PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(255),
    country CHAR(2) NOTNULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN'))
);