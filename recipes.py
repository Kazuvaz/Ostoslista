
import sqlite3
import db
def add_recipe(name, ingridients, user_id):
    try:
        sql = "INSERT INTO recipes (title , ingridients, user_id) VALUES (?, ?, ?)"
        db.execute(sql, [name, ingridients, user_id])
    except sqlite3.IntegrityError:
        return "wtf"
def get_my_recipes(user_id):
    sql = "SELECT id, title, ingridients FROM recipes WHERE user_id=? ORDER BY id DESC"
    
    return db.query(sql,[user_id])
def get_recipe(recipe_id):
    sql = "SELECT title, ingridients FROM recipes WHERE id=?"
    return db.query(sql,[recipe_id])[0]
    