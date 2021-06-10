import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get(
                "confirm_password"))
        }
        mongo.db.users.insert_one(signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/display_recipe/<task_id>", methods=["GET", "POST"])
def display_recipe(task_id):
    task = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
    steps = task.get("steps")
    step1 = steps[0]
    step2 = steps[1]
    step3 = steps[2]
    step4 = steps[3]
    step5 = steps[4]
    step6 = steps[5]
    step7 = steps[6]
    step8 = steps[7]
    step9 = steps[8]
    step10 = steps[9]
    return render_template(
        "display_recipe.html",
        task=task, step1=step1, step2=step2, step3=step3,
        step4=step4, step5=step5, step6=step6, step7=step7,
        step8=step8, step9=step9, step10=step10)


@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        steps = []
        if request.form.get("step1") != "":
            steps.append(request.form.get("step1"))
        else:
            steps.append("#blank")
        if request.form.get("step2") != "":
            steps.append(request.form.get("step2"))
        else:
            steps.append("#blank")
        if request.form.get("step3") != "":
            steps.append(request.form.get("step3"))
        else:
            steps.append("#blank")
        if request.form.get("step4") != "":
            steps.append(request.form.get("step4"))
        else:
            steps.append("#blank")
        if request.form.get("step5") != "":
            steps.append(request.form.get("step5"))
        else:
            steps.append("#blank")
        if request.form.get("step6") != "":
            steps.append(request.form.get("step6"))
        else:
            steps.append("#blank")
        if request.form.get("step7") != "":
            steps.append(request.form.get("step7"))
        else:
            steps.append("#blank")
        if request.form.get("step8") != "":
            steps.append(request.form.get("step8"))
        else:
            steps.append("#blank")
        if request.form.get("step9") != "":
            steps.append(request.form.get("step9"))
        else:
            steps.append("#blank")
        if request.form.get("step10") != "":
            steps.append(request.form.get("step10"))
        else:
            steps.append("#blank")
        task = {
            "main_component_type": request.form.get("select1"),
            "drink_name": request.form.get("drink_name"),
            "ingredients": request.form.get("ingredients-input"),
            "allergen_warning": request.form.get("select"),
            "image_url": request.form.get("image-url"),
            "recommends": 0,
            "preparation_time": request.form.get("select3"),
            "difficulty_level": request.form.get("select2"),
            "created_by": session["user"],
            "user_likes": (""),
            "steps": steps
        }
        mongo.db.recipes.insert_one(task)
        flash("Your New Recipe Was Added")
        return redirect(url_for("new_recipe"))

    return render_template("new_recipe.html")


@app.route("/edit_recipe/<task_id>", methods=["GET", "POST"])
def edit_recipe(task_id):
    if request.method == "POST":
        likes = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
        steps = []
        if request.form.get("step1") != "":
            steps.append(request.form.get("step1"))
        else:
            steps.append("#blank")
        if request.form.get("step2") != "":
            steps.append(request.form.get("step2"))
        else:
            steps.append("#blank")
        if request.form.get("step3") != "":
            steps.append(request.form.get("step3"))
        else:
            steps.append("#blank")
        if request.form.get("step4") != "":
            steps.append(request.form.get("step4"))
        else:
            steps.append("#blank")
        if request.form.get("step5") != "":
            steps.append(request.form.get("step5"))
        else:
            steps.append("#blank")
        if request.form.get("step6") != "":
            steps.append(request.form.get("step6"))
        else:
            steps.append("#blank")
        if request.form.get("step7") != "":
            steps.append(request.form.get("step7"))
        else:
            steps.append("#blank")
        if request.form.get("step8") != "":
            steps.append(request.form.get("step8"))
        else:
            steps.append("#blank")
        if request.form.get("step9") != "":
            steps.append(request.form.get("step9"))
        else:
            steps.append("#blank")
        if request.form.get("step10") != "":
            steps.append(request.form.get("step10"))
        else:
            steps.append("#blank")
        submit = {
            "main_component_type": request.form.get("select1"),
            "drink_name": request.form.get("drink_name"),
            "ingredients": request.form.get("ingredients-input"),
            "allergen_warning": request.form.get("select"),
            "image_url": request.form.get("image-url"),
            "recommends": int(likes.get("recommends")),
            "preparation_time": request.form.get("select3"),
            "difficulty_level": request.form.get("select2"),
            "created_by": session["user"],
            "user_likes": likes.get("user_likes"),
            "steps": steps
        }
        mongo.db.recipes.update({"_id": ObjectId(task_id)}, submit)
        flash("Recipe Successfully Updated")

    task = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
    steps = task.get("steps")
    if steps[0] == "#blank":
        step1 = ""
    else:
        step1 = steps[0]
    if steps[1] == "#blank":
        step2 = ""
    else:
        step2 = steps[1]
    if steps[2] == "#blank":
        step3 = ""
    else:
        step3 = steps[2]
    if steps[3] == "#blank":
        step4 = ""
    else:
        step4 = steps[3]
    if steps[4] == "#blank":
        step5 = ""
    else:
        step5 = steps[4]
    if steps[5] == "#blank":
        step6 = ""
    else:
        step6 = steps[5]
    if steps[6] == "#blank":
        step7 = ""
    else:
        step7 = steps[6]
    if steps[7] == "#blank":
        step8 = ""
    else:
        step8 = steps[7]
    if steps[8] == "#blank":
        step9 = ""
    else:
        step9 = steps[8]
    if steps[9] == "#blank":
        step10 = ""
    else:
        step10 = steps[9]
    return render_template(
        "edit_recipe.html",
        task=task, step1=step1, step2=step2, step3=step3,
        step4=step4, step5=step5, step6=step6, step7=step7,
        step8=step8, step9=step9, step10=step10)


@app.route("/delete_recipe/<task_id>")
def delete_recipe(task_id):
    mongo.db.recipes.remove({"_id": ObjectId(task_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/update_likes/<task_id>", methods=["GET", "POST"])
def update_likes(task_id):
    likes = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
    search_user = likes.get("user_likes")
    if session["user"] not in search_user:
        like = likes.get("recommends")
        new_val = int(like) + 1
        user_likes = likes.get("user_likes")
        user_likes = (user_likes + session["user"] + ", ")
        submit = {
            "main_component_type": likes.get("main_component_type"),
            "drink_name": likes.get("drink_name"),
            "ingredients": likes.get("ingredients"),
            "allergen_warning": likes.get("allergen_warning"),
            "image_url": likes.get("image_url"),
            "recommends": new_val,
            "preparation_time": likes.get("preparation_time"),
            "difficulty_level": likes.get("difficulty_level"),
            "created_by": likes.get("created_by"),
            "user_likes": user_likes,
            "steps": likes.get("steps")
        }
        mongo.db.recipes.update({"_id": ObjectId(task_id)}, submit)
        task = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
        steps = task.get("steps")
        step1 = steps[0]
        step2 = steps[1]
        step3 = steps[2]
        step4 = steps[3]
        step5 = steps[4]
        step6 = steps[5]
        step7 = steps[6]
        step8 = steps[7]
        step9 = steps[8]
        step10 = steps[9]
        return render_template(
            "display_recipe.html",
            task=task, step1=step1, step2=step2, step3=step3,
            step4=step4, step5=step5, step6=step6, step7=step7,
            step8=step8, step9=step9, step10=step10)

    task = mongo.db.recipes.find_one({"_id": ObjectId(task_id)})
    steps = task.get("steps")
    step1 = steps[0]
    step2 = steps[1]
    step3 = steps[2]
    step4 = steps[3]
    step5 = steps[4]
    step6 = steps[5]
    step7 = steps[6]
    step8 = steps[7]
    step9 = steps[8]
    step10 = steps[9]
    return render_template(
        "display_recipe.html",
        task=task, step1=step1, step2=step2, step3=step3,
        step4=step4, step5=step5, step6=step6, step7=step7,
        step8=step8, step9=step9, step10=step10)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# Update the debug=True to debug=False prior to submission
