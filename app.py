from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from flask_wtf import CSRFProtect
import os
from collections import defaultdict
import re
from datetime import datetime, timedelta
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
load_dotenv()
import secrets

app = Flask(__name__)
# csrf = CSRFProtect(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "fallback-super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app = Flask(__name__)
# csrf = CSRFProtect(app)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 🔐 Production Security Settings
if os.environ.get("ENV") == "production":
    app.config["SESSION_COOKIE_SECURE"] = True
    app.config["REMEMBER_COOKIE_SECURE"] = True
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["REMEMBER_COOKIE_HTTPONLY"] = True

oauth = OAuth(app)
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

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
    reset_token = db.Column(db.String(200), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")
    
    email_verified = db.Column(db.Boolean, default=False)

    verification_token = db.Column(db.String(200), nullable=True)
    verification_token_expiry = db.Column(db.DateTime, nullable=True)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    author = db.relationship("User", backref="posts")
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
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose another.")
            return redirect(url_for("register"))

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

        print("\n==== EMAIL VERIFICATION LINK ====")
        print(f"http://127.0.0.1:5000/verify-email/{token}")
        print("==== END LINK ====\n")

        flash("Account created. Please verify your email.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter(
            (User.username == username) | (User.email == username)
        ).first()

        if user and check_password_hash(user.password, password):

            if not user.email_verified:
                flash("Please verify your email before logging in.")
                return redirect(url_for("login"))

            login_user(user)
            return redirect("/community")

        else:
            flash("Invalid credentials")

    return render_template("auth.html")
@app.route("/login/google")
def google_login():
    redirect_uri = url_for("google_callback", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/google/callback")
def google_callback():
    token = google.authorize_access_token()
    user_info = token.get("userinfo")

    if not user_info:
        user_info = google.get("userinfo").json()

    email = user_info["email"]

    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(
            username=email.split("@")[0],
            email=email,
            password=generate_password_hash(secrets.token_urlsafe(16)),
            email_verified=True
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect("/community")
    redirect_uri = url_for("google_callback", _external=True)
    return google.authorize_redirect(redirect_uri)
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
    return render_template("community.html", posts=posts)


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":
        post = Post(
            title=request.form["title"],
            content=request.form["content"],
            user_id=current_user.id,
        )
        db.session.add(post)
        db.session.commit()
        return redirect("/community")

    return render_template("create.html")

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
# ================= FORGOT PASSWORD =================

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")

        user = User.query.filter_by(email=email).first()

        if user:
            token = secrets.token_urlsafe(32)
            expiry = datetime.utcnow() + timedelta(minutes=15)

            user.reset_token = token
            user.reset_token_expiry = expiry
            db.session.commit()

            print("\n==== PASSWORD RESET LINK ====")
            print(f"http://127.0.0.1:5000/reset-password/{token}")
            print("==== END LINK ====\n")

            flash("Reset link generated. Check server console.")
        else:
            flash("Email not found.")

    return render_template("forgot_password.html")

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

# ================= EDIT COMMENT =================

@app.route("/comment/<int:comment_id>/edit", methods=["GET", "POST"])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    if request.method == "POST":
        comment.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("post_detail", post_id=comment.post_id))

    return render_template("edit_comment.html", comment=comment)


# ================= DELETE COMMENT =================

@app.route("/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    post_id = comment.post_id
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for("post_detail", post_id=post_id))

# ================= EMAIL VERIFICATION =================

@app.route("/verify-email/<token>")
def verify_email(token):
    user = User.query.filter_by(verification_token=token).first()

    if not user:
        return "Invalid or expired verification link."

    if user.verification_token_expiry < datetime.utcnow():
        return "Verification link expired."

    user.email_verified = True
    user.verification_token = None
    user.verification_token_expiry = None

    db.session.commit()

    flash("Email verified successfully. You can now login.")
    return redirect(url_for("login"))

# ================= RESET PASSWORD =================

@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()

    if not user:
        return "Invalid or expired token."

    if user.reset_token_expiry < datetime.utcnow():
        return "Token expired."

    if request.method == "POST":
        new_password = request.form.get("password")

        user.password = generate_password_hash(new_password)
        user.reset_token = None
        user.reset_token_expiry = None

        db.session.commit()

        flash("Password reset successful. Please login.")
        return redirect(url_for("login"))

    return render_template("reset_password.html")

# ================= DB INIT =================

with app.app_context():
    db.create_all()


# ================= START SERVER =================

if __name__ == "__main__":
    app.run(debug=False)