import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash 

import config
import db
import recipes
import secrets
import users
app = Flask(__name__)
app.secret_key = config.secret_key

def check_csrf():
    
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)
@app.route("/")
def index():
    
    
    return render_template("index.html")

@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    
    return render_template("edit_recipe.html", recipe =recipe)

@app.route("/follow_recipe/<int:recipe_id>")
def follow_recipe(recipe_id):
    
    
    recipes.follow_recipe(session["user_id"],recipe_id)
    return redirect("/other_recipies")

@app.route("/unfollow_recipe/<int:recipe_id>")
def unfollow_recipe(recipe_id):
    recipes.unfollow_recipe(session["user_id"],recipe_id)
    return redirect("/other_recipies")

@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    has = not recipes.already_follow(session["user_id"],recipe_id)
    count = recipes.count_followers(recipe_id)
    return render_template("show_recipe.html", recipe =recipe, has =has, count =count)

@app.route("/my_recipies")
def my_recipies():
    my_recipes = recipes.get_my_recipes(session["user_id"])
    return render_template("my_recipies.html", recipes=my_recipes)

@app.route("/other_recipies")
def others_recipies():
    my_recipes = recipes.get_others_recipes(session["user_id"])
    return render_template("my_recipies.html", recipes=my_recipes)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    check_csrf()
    recipe_name = request.form["recipe_name"]
    recipe_ingridients = request.form["ingridients"]
    user_id = session["user_id"]
    recipes.add_recipe(recipe_name,recipe_ingridients, user_id)
    return redirect("/")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        users.create_account(username,password_hash)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":    
        username = request.form["username"]
        password = request.form["password"]
        
        result = users.get_hash(username)
        user_id = result["id"]
        password_hash = result["password_hash"]
       

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/login")

@app.route("/new_recipe")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/update_recipe", methods=["POST"])
def update_recipe():
    check_csrf()
    recipe_id =  request.form["recipe_id"]
    recipe_name = request.form["recipe_name"]
    recipe_ingridients = request.form["ingridients"]
    
    recipes.update_recipe(recipe_id,recipe_name,recipe_ingridients)
    return redirect("/recipe/" + str(recipe_id))

@app.route("/remove_recipe/<int:recipe_id>")
def remove_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    
    return render_template("remove_recipe.html", recipe =recipe)

@app.route("/delete_recipe", methods=["POST"])
def delete_recipe():
    check_csrf()
    recipe_id =  request.form["recipe_id"]
    
    recipes.delete_recipe(recipe_id)
    return redirect("/my_recipies")
    
