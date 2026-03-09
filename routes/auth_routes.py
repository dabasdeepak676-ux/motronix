from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from datetime import datetime, timedelta

from models.models import db, User

auth_bp = Blueprint("auth", __name__)


ADMIN_EMAILS = [
"dabasdeepak676@gmail.com",
"riteshsingh1609@gmail.com",
"channelspeed16@gmail.com",
"mechanicalbull@gmail.com"
]


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash("Username already exists.")
            return redirect(url_for("auth.register"))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Email already registered.")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        token = secrets.token_urlsafe(32)
        expiry = datetime.utcnow() + timedelta(minutes=30)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            role="user",
            email_verified=False,
            verification_token=token,
            verification_token_expiry=expiry
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully.")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter(
            (User.username == username) | (User.email == username)
        ).first()

        if user and check_password_hash(user.password, password):

            if user.email in ADMIN_EMAILS:
                user.role = "admin"
                db.session.commit()

            if user.is_banned:
                flash("Your account has been banned.")
                return redirect(url_for("auth.login"))

            if not user.email_verified:
                flash("Please verify your email before logging in.")
                return redirect(url_for("auth.login"))

            login_user(user)

            return redirect("/community")

        else:
            flash("Invalid credentials")

    return render_template("auth.html")


@auth_bp.route("/logout")
def logout():

    logout_user()

    flash("You have been logged out.")

    return redirect("/")