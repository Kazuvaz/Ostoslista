
import sqlite3
import db
def add_recipe(name, ingridients, user_id):
    
    sql = "INSERT INTO recipes (title , ingridients, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [name, ingridients, user_id])
def get_my_recipes(user_id):
    sql = "SELECT id, title, ingridients FROM recipes WHERE user_id=? ORDER BY id DESC"
    
    return db.query(sql,[user_id])
def get_recipe(recipe_id):
    sql = "SELECT id, title, ingridients, user_id FROM recipes WHERE id=?"
    return db.query(sql,[recipe_id])[0]
def update_recipe(id,name,ingridients):
    sql = "UPDATE recipes SET title = ?, ingridients = ? WHERE id =?"
    db.execute(sql, [name, ingridients, id])
def delete_recipe(id):
    sql = "DELETE FROM recipes WHERE id =?"
    db.execute(sql, [id])

    