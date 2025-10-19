
import sqlite3
import db

def update_ingridients(recipe_id, ingridient_text : str):
    sql = "DELETE FROM recipes WHERE recipe_id=?"
    db.execute(sql, [recipe_id])
    create_ingridients(recipe_id, ingridient_text)

def create_ingridients(recipe_id, ingridient_text : str):
    splat = ingridient_text.split(",")
    
    for a in splat:
        amount = 0
        words = a.split(" ")
        if len(words) >1:
            try:
                amount = int(words[len(words)-1])
            except:
                amount = 1
        name = words[0]
        for i in range(1,len(words)-1):
            name += str(words[i])
        sql = "INSERT INTO ingridients (ingridient_name, amount, recipe_id) VALUES (?, ?, ?)"
        db.execute(sql, [name,amount,recipe_id])
        
def get_all_ingridients(user_id):
    sql ="""SELECT ingridient_name, amount FROM ingridients a
        INNER JOIN recipes b ON a.recipe_id = b.id
        INNER JOIN subscriptions c ON b.id = c.recipe_id
        WHERE user_id=?
        """
    quer = db.query(sql,[user_id])
    d = {}
    for a in quer:
        if a[0] in d:
            d[a[0]] += int(a[1])
        else:
            d[a[0]] = a[1]
    #wasnt sure how to go through dictionary on html side so i just converted it into nested array
    nes = []
    for v in d:
        nes.append([v,d[v]])
    return nes
    

    
