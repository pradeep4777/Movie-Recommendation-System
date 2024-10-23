from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_migrate import Migrate
from recommendation import get_movie_recommendations
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            flash(
                "Username or Email already exists. Please try again with a different one.",
                "danger",
            )
            return redirect(url_for("register"))
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully! Please login.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["username"] = user.username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed. Check email and password.", "danger")

    return render_template("login.html")


# Home page 
@app.route("/home", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        movie_name = request.form["movie_name"]
        recommendations = get_movie_recommendations(movie_name)
        return render_template("recommendations.html", recommendations=recommendations)

    return render_template("home.html")


# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
