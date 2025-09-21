CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE recipes (
    id Integer PRIMARY KEY,	
	title TEXT,
    ingridients TEXT,
    user_id Integer REFERENCES users 
);
