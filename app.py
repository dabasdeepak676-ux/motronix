from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from flask_wtf import CSRFProtect
import os
from collections import defaultdict
import re

app = Flask(__name__)
# csrf = CSRFProtect(app)
app.config["SECRET_KEY"] = "motronix-super-secure-2026"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

UPLOAD_FOLDER = "static/news_images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

db = SQLAlchemy(app)

conversation_memory = defaultdict(list)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
# ================= AUTOHIVE KNOWLEDGE BASE =================

KNOWLEDGE_BASE = {

    "buying": {
        "city": "For city driving choose compact car, light steering, good visibility and automatic transmission.",
        "highway": "For highway choose stable chassis, strong braking, minimum 4-star safety and refined engine.",
        "default": "Choose car based on usage: City → Hatchback, Highway → Sedan, Bad roads → Compact SUV. Always check service cost and resale."
    },

    "service": {
        "default": "Service warning ⚠️ Always ask for old parts back. Avoid unnecessary throttle cleaning and early brake replacement."
    },

    "gear": {
        "morning": "Morning hard gear shift usually happens due to cold transmission oil. If it improves after 5–10 min, it's normal.",
        "default": "Hard gear shift can be due to clutch wear or low transmission oil. Avoid half-clutch driving."
    },

    "engine": {
        "vibration": "Engine vibration may indicate mounting issue, misfire or fuel quality problem. Do not ignore.",
        "default": "Engine noise can be due to low oil, timing belt wear or tappet issue."
    },

    "ev": {
        "default": "EV is best for city usage. Check 8-year battery warranty and charging availability in your area."
    }

}

# ================= MODELS =================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    author = db.relationship("User", backref="posts")
    category = db.relationship("Category", backref="posts")
    comments = db.relationship("Comment", backref="post", cascade="all, delete")
    votes = db.relationship("Vote", backref="post", cascade="all, delete")


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

    user = db.relationship("User", backref="comments")


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=db.func.now())


# ================= LOGIN =================

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose another.")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed_password,
            role="user"
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully. Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/community")
        else:
            flash("Invalid credentials")

    return render_template("auth.html")
@app.route("/make-admin")
def make_admin():
    user = User.query.first()
    user.role = "admin"
    db.session.commit()
    return "Admin assigned"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


# ================= COMMUNITY =================

@app.route("/community")
def community():
    posts = Post.query.order_by(Post.id.desc()).all()
    categories = Category.query.all()
    return render_template("community.html", posts=posts, categories=categories)


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    categories = Category.query.all()

    if request.method == "POST":
        post = Post(
            title=request.form["title"],
            content=request.form["content"],
            user_id=current_user.id,
            category_id=int(request.form["category"])
        )
        db.session.add(post)
        db.session.commit()
        return redirect("/community")

    return render_template("create.html", categories=categories)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("post_detail", post_id=post.id))

    return render_template("edit.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("community"))


@app.route("/add_comment/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    content = request.form.get("content")

    if content:
        new_comment = Comment(
            content=content,
            user_id=current_user.id,
            post_id=post_id
        )
        db.session.add(new_comment)
        db.session.commit()

    return redirect(url_for("post_detail", post_id=post_id))


@app.route("/upvote/<int:post_id>")
@login_required
def upvote(post_id):
    existing_vote = Vote.query.filter_by(
        user_id=current_user.id,
        post_id=post_id
    ).first()

    if existing_vote:
        db.session.delete(existing_vote)
    else:
        db.session.add(Vote(user_id=current_user.id, post_id=post_id))

    db.session.commit()
    return redirect("/community")


# ================= NEWS =================

@app.route("/news")
def news_list():
    news_items = News.query.order_by(News.created_at.desc()).all()
    return render_template("news.html", news_items=news_items)


@app.route("/news/<int:news_id>")
def news_detail(news_id):
    news = News.query.get_or_404(news_id)
    return render_template("news_detail.html", news=news)


@app.route("/admin/news/create", methods=["GET", "POST"])
@login_required
def create_news():
    if current_user.id != 1:
        return "Unauthorized"

    if request.method == "POST":
        image_file = request.files.get("image")
        filename = None

        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        news = News(
            title=request.form["title"],
            content=request.form["content"],
            image=filename
        )

        db.session.add(news)
        db.session.commit()
        return redirect("/news")

    return render_template("create_news.html")

from flask import jsonify
import requests
# ================= CLEAN FOLLOW-UP AI =================

followup_state = {}

@app.route("/ask-ai", methods=["POST"])
@login_required
def ask_ai():

    data = request.get_json()
    user_message = data.get("message", "").lower()
    user_id = current_user.id

    # ===== Follow-up Answer =====
    if user_id in followup_state:

        topic = followup_state[user_id]
        del followup_state[user_id]

        if topic == "gear":

            if "morning" in user_message:
                return jsonify({
                    "reply": """🔍 Gear Issue:
Morning me hard gear cold transmission oil ki wajah se hota hai.

🛠 Advice:
5–10 min smooth drive karo.
Warm hone ke baad smooth ho jaye to normal hai.

⚠ Warning:
Grinding sound aaye to mechanic dikhao.
"""
                })
            else:
                return jsonify({
                    "reply": """⚠ Gear Problem Serious Ho Sakta Hai:
Agar har time hard hai to clutch ya gearbox issue ho sakta hai.

Inspection karwana better hai.
"""
                })

    # ===== First Question Detection =====
    if "gear" in user_message or "clutch" in user_message:

        followup_state[user_id] = "gear"

        return jsonify({
            "reply": "Ye problem morning me hoti hai ya har time? 🤔"
        })

    return jsonify({
        "reply": "Buying, service, engine ya EV ke baare me pooch sakte ho."
    })

with app.app_context():
    db.create_all()
    
# ================= INIT =================

if __name__ == "__main__":
    app.run(debug=True)