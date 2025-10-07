CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE recipes (
    id Integer PRIMARY KEY,	
	title TEXT,
    ingridients TEXT,
    owner_id Integer REFERENCES users 
); 

CREATE TABLE subscriptions (
    user_id Integer REFERENCES users,
    recipe_id Integer REFERENCES recipes
);
