-- It should be noted that this is a mock-up representation of the SQLite database that exists. Django handles the automatic creation and modification of the database via Python code that we write.

-- User Table
CREATE TABLE IF NOT EXISTS UserTable (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL, 
    username VARCHAR(150) NOT NULL UNIQUE, 
    password VARCHAR(128) NOT NULL, 
    email VARCHAR(254) NOT NULL, 
    date_joined datetime NOT NULL, 
    last_login datetime NULL
);

-- US State Table
CREATE TABLE IF NOT EXISTS USStateTable (
    abbreviation VARCHAR(2) NOT NULL,
    state_name VARCHAR(30) NOT NULL
);

INSERT INTO USStateTable (state_name, abbreviation)
VALUES
("Alabama", 'AL'),
("Alaska", 'AK'),
("Arizona", 'AZ'),
("Arkansas", 'AR'),
("California", 'CA'),
("Colorado", 'CO'),
("Connecticut", 'CT'),
("Delaware", 'DE'),
("Florida", 'FL'),
("Georgia", 'GA'),
("Hawaii", 'HI'),
("Idaho", 'ID'),
("Illinois", 'IL' ),
("Indiana", 'IN'),
("Iowa", 'IA'),
("Kansas", 'KS'),
("Kentucky", 'KY'),
("Louisiana", 'LA'),
("Maine", 'ME'),
("Maryland", 'MD' ),
("Massachusetts", 'MA' ),
("Michigan", 'MI'),
("Minnesota", 'MN'),
("Mississippi", 'MS'),
("Missouri", 'MO'),
("Montana", 'MT'),
("Nebraska", 'NE'),
("Nevada", 'NV'),
("NewHampshire", 'NH' ),
("NewJersey", 'NJ'),
("NewMexico", 'NM'),
("NewYork", 'NY'),
("NorthCarolina", 'NC' ),
("NorthDakota", 'ND'),
("Ohio", 'OH'),
("Oklahoma", 'OK' ),
("Oregon", 'OR'),
("Pennsylvania", 'PA' ),
("RhodeIsland", 'RI'),
("SouthCarolina", 'SC'),
("SouthDakota", 'SD'),
("Tennessee", 'TN'),
("Texas", 'TX'),
("Utah", 'UT'),
("Vermont", 'VT'),
("Virginia", 'VA'),
("Washington", 'WA'),
("WestVirginia", 'WV'),
("Wisconsin", 'WI'),
("Wyoming", 'WY');

-- Fuel Quote Table
CREATE TABLE IF NOT EXISTS FuelQuoteTable(
    user_id INTEGER,
    quote_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	gallons_requested FLOAT NOT NULL,
    delivery_address VARCHAR(150) NOT NULL,
    delivery_date datetime NULL,
    total_amount_due FLOAT NOT NULL
);
ALTER TABLE FuelQuoteTable
ADD FOREIGN KEY (user_id) REFERENCES UserTable(user_id);

-- Fuel Quote History
SELECT * FROM FuelQuoteTable WHERE user_id=000;

-- Client Profile Table
CREATE TABLE IF NOT EXISTS ClientProfileTable(
    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    address1 VARCHAR(100) NOT NULL,
    address2 VARCHAR(100),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(2) NOT NULL,
    zipcode INTEGER(9) NOT NULL
);
ALTER TABLE ClientProfileTable
ADD FOREIGN KEY (user_id) REFERENCES UserTable(user_id);