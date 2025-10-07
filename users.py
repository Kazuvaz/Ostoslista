
import sqlite3
import db

def create_account(username, password_hash):
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])
def get_hash(username):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    return  db.query(sql, [username])[0]

    