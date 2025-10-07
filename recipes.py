
import sqlite3
import db
def add_recipe(name, ingridients, user_id):
    
    sql = "INSERT INTO recipes (title , ingridients, owner_id) VALUES (?, ?, ?)"
    db.execute(sql, [name, ingridients, user_id])

    #tällä hetkellä jos kahdella reseptillä on sama nimi voi yhdistys tulla väärän reseptin kanssa 
    sql = "SELECT id FROM recipes WHERE title=?"
    recipe_id = db.query(sql,[name])[0][0]

    sql = "INSERT INTO subscriptions (user_id, recipe_id) VALUES (?, ?)"
    db.execute(sql, [user_id,recipe_id])
def get_my_recipes(user_id):
    sql = """SELECT id, title, ingridients 
        FROM recipes 
        INNER JOIN subscriptions on recipe_id = id 
        WHERE user_id=? ORDER BY id DESC"""
    
    return db.query(sql,[user_id])
def get_others_recipes(user_id):
    sql = "SELECT id, title, ingridients FROM recipes WHERE owner_id!=? "
    
    return db.query(sql,[user_id])
def get_recipe(recipe_id):
    sql = "SELECT id, title, ingridients, owner_id FROM recipes WHERE id=?"
    return db.query(sql,[recipe_id])[0]
def update_recipe(id,name,ingridients):
    sql = "UPDATE recipes SET title = ?, ingridients = ? WHERE id =?"
    db.execute(sql, [name, ingridients, id])
def delete_recipe(id):
    sql = "DELETE FROM recipes WHERE id =?"
    db.execute(sql, [id])
def follow_recipe(user_id,recipe_id):
    sql = "INSERT INTO subscriptions (user_id, recipe_id) VALUES (?, ?)"
    db.execute(sql, [user_id,recipe_id])
def unfollow_recipe(user_id,recipe_id):
    sql = "DELETE FROM subscriptions WHERE user_id=? AND recipe_id=?"
    db.execute(sql,[user_id,recipe_id])
def already_follow(user_id,recipe_id):
    sql = "SELECT * FROM subscriptions WHERE user_id=? AND recipe_id=?"
    res = db.query(sql,[user_id,recipe_id])
    return (len(res) >0)
def count_followers(recipe_id):
    sql = "SELECT * FROM subscriptions WHERE recipe_id=?"
    res = db.query(sql,[recipe_id])
    return len(res)

    


    