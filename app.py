from dotenv import load_dotenv
load_dotenv()
from ai_engine.diagnostic_engine import diagnose_vehicle
from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from flask_wtf import CSRFProtect
import os
from collections import defaultdict
from google import genai
import re
from datetime import datetime, timedelta

from ai_engine.diagnostic_engine import diagnose_vehicle
from authlib.integrations.flask_client import OAuth

import secrets

def ai_diagnose(problem, car):

    problem = problem.lower()

    results = []

    # Brake vibration
    if "vibration" in problem and "brake" in problem:

        results.append({
            "issue": "Brake Disc Warp",
            "confidence": 78,
            "reason": "Vibration during braking often indicates warped brake discs."
        })

        results.append({
            "issue": "Brake Pad Wear",
            "confidence": 52,
            "reason": "Uneven brake pad wear can cause vibration."
        })

        results.append({
            "issue": "Wheel Balancing",
            "confidence": 31,
            "reason": "Improper wheel balance may create vibration."
        })

    # Engine vibration
    elif "vibration" in problem:

        results.append({
            "issue": "Engine Mount Damage",
            "confidence": 70,
            "reason": "Engine mounts absorb vibration."
        })

        results.append({
            "issue": "Wheel Balancing",
            "confidence": 45,
            "reason": "Wheel imbalance can cause vibration."
        })

    # Noise issues
    elif "noise" in problem or "sound" in problem:

        results.append({
            "issue": "Suspension Wear",
            "confidence": 65,
            "reason": "Suspension components often produce noise."
        })

        results.append({
            "issue": "Bearing Damage",
            "confidence": 50,
            "reason": "Wheel bearings may create humming noise."
        })

    # Overheating
    elif "overheat" in problem or "temperature" in problem:

        results.append({
            "issue": "Low Coolant",
            "confidence": 75,
            "reason": "Low coolant commonly causes overheating."
        })

        results.append({
            "issue": "Radiator Blockage",
            "confidence": 40,
            "reason": "Blocked radiator reduces cooling."
        })

    else:

        results.append({
            "issue": "Unknown Issue",
            "confidence": 20,
            "reason": "Problem needs manual inspection."
        })

    return results

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
ADMIN_EMAILS = [
    "dabasdeepak676@gmail.com",
    "riteshsingh1609@gmail.com"
]
@app.context_processor
def inject_admin_emails():
    return dict(ADMIN_EMAILS=ADMIN_EMAILS)
    
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = ("Motronix", os.environ.get("MAIL_FROM"))

mail = Mail(app)

# csrf = CSRFProtect(app)

# ===============================
# DATABASE CONFIG (LOCAL + PROD)
# ===============================

database_url = os.environ.get("DATABASE_URL")

if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "super-secret-dev-key-123"

app.config["SQLALCHEMY_DATABASE_URI"] = database_url or "sqlite:///database.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# 🔐 Production Security Settings
if os.environ.get("ENV") == "production":
    app.config["SESSION_COOKIE_SECURE"] = True
    app.config["REMEMBER_COOKIE_SECURE"] = True
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["REMEMBER_COOKIE_HTTPONLY"] = True

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


UPLOAD_FOLDER = "static/news_images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

PROFILE_UPLOAD = "static/profile_images"
app.config["PROFILE_UPLOAD"] = PROFILE_UPLOAD

if not os.path.exists(PROFILE_UPLOAD):
    os.makedirs(PROFILE_UPLOAD)

@app.route("/update-profile", methods=["POST"])
@login_required
def update_profile():

    current_user.city = request.form.get("city")
    current_user.state = request.form.get("state")
    current_user.country = request.form.get("country")
    current_user.pincode = request.form.get("pincode")
    current_user.mobile = request.form.get("mobile")

    photo = request.files.get("profile_photo")

    if photo and photo.filename != "":
        filename = secure_filename(photo.filename)

        save_path = os.path.join(app.config["PROFILE_UPLOAD"], filename)

        photo.save(save_path)

        current_user.profile_photo = filename

    db.session.commit()

    flash("Profile updated successfully")

    return redirect("/profile")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

conversation_memory = defaultdict(list)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from email.header import Header

def send_email(to, subject, body):
    try:
        print("SENDING EMAIL TO:", to)

        msg = Message(
            subject=subject,
            recipients=[to],
            body=body,
            sender=("Motronix", os.environ.get("MAIL_FROM"))
        )

        mail.send(msg)

        print("EMAIL SENT SUCCESSFULLY")

    except Exception as e:
        print("EMAIL ERROR:", e)

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
    mobile = db.Column(db.String(20))

    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    role = db.Column(db.String(20), default="user")

    ai_uses_today = db.Column(db.Integer, default=0)
    ai_last_reset = db.Column(db.DateTime)

    email_verified = db.Column(db.Boolean, default=False)
    is_banned = db.Column(db.Boolean, default=False)

    reset_token = db.Column(db.String(200), nullable=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)

    verification_token = db.Column(db.String(200), nullable=True)
    verification_token_expiry = db.Column(db.DateTime, nullable=True)

    profile_photo = db.Column(db.String(200))

    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    pincode = db.Column(db.String(20))

    
    reputation = db.Column(db.Integer, default=0)
    posts_count = db.Column(db.Integer, default=0)
    helpful_answers = db.Column(db.Integer, default=0)
    badge = db.Column(db.String(50), default="Member")

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

# ================= REPUTATION SYSTEM =================

def update_user_reputation(user):

    user.reputation = user.posts_count * 5 + user.helpful_answers * 10

    if user.reputation >= 500:
        user.badge = "Master"

    elif user.reputation >= 200:
        user.badge = "Expert"

    elif user.reputation >= 50:
        user.badge = "Contributor"

    else:
        user.badge = "Member"


# ================= CAR MODEL =================

class Car(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)

    fuel_type = db.Column(db.String(50))
    mileage = db.Column(db.Integer)

    is_default = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    owner = db.relationship(
        "User",
        backref="cars"
    )

# ================= LOGIN =================

@login_manager.user_loader
def load_user(user_id):
    user = db.session.get(User, int(user_id))
    if user:
        return user
    return None

# ================= ROUTES =================

@app.route("/")
@login_required
def home():

    cars = Car.query.filter_by(owner_id=current_user.id).all()

    default_car = Car.query.filter_by(
        owner_id=current_user.id,
        is_default=True
    ).first()

    return render_template(
        "home.html",
        default_car=default_car,
        cars=cars
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash("Username already exists.")
            return redirect(url_for("register"))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Email already registered. Please login.")
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

        verification_link = url_for("verify_email", token=token, _external=True)

        send_email(
            to=email,
            subject="Verify your Motronix account",
            body=f"Click this link to verify your account:\n\n{verification_link}"
        )

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
            # Auto admin assign
            if user.email in ADMIN_EMAILS:
             user.role = "admin"
             db.session.commit()
            if user.is_banned:
              flash("Your account has been banned.")
              return redirect(url_for("login"))

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

    # ✅ Admin assignment after user exists
    if user.email in ADMIN_EMAILS:
        user.role = "admin"
        db.session.commit()

    login_user(user)

    return redirect("/community")

@app.route("/make-admin")
def make_admin():

    user = User.query.order_by(User.id.desc()).first()

    if user:
        user.role = "admin"
        db.session.commit()
        return "Admin assigned"

    return "No user found"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect("/")

@app.route("/profile")
@login_required
def profile():

    cars_count = Car.query.filter_by(owner_id=current_user.id).count()

    posts_count = Post.query.filter_by(user_id=current_user.id).count()

    ai_used = current_user.ai_uses_today

    return render_template(
        "profile.html",
        cars_count=cars_count,
        posts_count=posts_count,
        ai_used=ai_used
    )


# ================= COMMUNITY =================

@app.route("/community")
@login_required
def community():

   posts = Post.query.order_by(Post.id.desc()).all()

   for post in posts:
       post.author = User.query.get(post.user_id)

   return render_template("community.html", posts=posts)
# ================= ADD CAR =================

@app.route("/add-car", methods=["GET", "POST"])
@login_required
def add_car():

    if request.method == "POST":

        brand = request.form["brand"]
        model = request.form["model"]
        year = request.form["year"]
        fuel = request.form["fuel"]
        mileage = request.form["mileage"]

        existing_car = Car.query.filter_by(owner_id=current_user.id).first()

        car = Car(
            owner_id=current_user.id,
            brand=brand,
            model=model,
            year=year,
            fuel_type=fuel,
            mileage=mileage,
            is_default=True if not existing_car else False
        )

        db.session.add(car)
        db.session.commit()

        return redirect("/garage")

    return render_template("add_car.html")


# ================= GARAGE =================

@app.route("/garage")
@login_required
def garage():

    cars = Car.query.filter_by(owner_id=current_user.id).all()

    return render_template("garage.html", cars=cars)


# ================= AI DIAGNOSE =================

@app.route("/diagnose", methods=["GET", "POST"])
@login_required
def diagnose():

    car = Car.query.first()

    if request.method == "POST":

        problem = request.form.get("problem")

        # collect answers from follow-up questions
        answers = {}

        for key in request.form:
            if key != "problem":
                answers[key] = request.form.get(key)

        results, questions = diagnose_vehicle(problem, answers)

        return render_template(
    "diagnosis_result.html",
    car=car,
    results=results,
    questions=questions,
    problem=problem
)

    return render_template("diagnose.html", car=car)
# ================= CREATE POST =================

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():

    if request.method == "POST":

        post = Post(
            title=request.form["title"],
            content=request.form["content"],
            user_id=current_user.id
        )

        db.session.add(post)

        current_user.posts_count += 1
        update_user_reputation(current_user)

        db.session.commit()

        return redirect("/community")

    return render_template("create.html")


# ================= POST DETAIL =================

@app.route("/post/<int:post_id>")
def post_detail(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("post_detail.html", post=post)


# ================= EDIT POST =================

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


# ================= DELETE POST =================

@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("community"))


# ================= ADD COMMENT =================

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


# ================= UPVOTE =================

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
    if current_user.role != "admin":
     return "Access Denied"

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
# ================= LEGAL PAGES =================

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
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

            reset_link = url_for("reset_password", token=token, _external=True)

            send_email(
                to=email,
                subject="Reset your Motronix password",
                body=f"Click this link to reset your password:\n\n{reset_link}"
            )

            flash("Reset link sent to your email.")
        else:
            flash("Email not found.")

    return render_template("forgot_password.html")

# ================= GEMINI DIAGNOSTIC AI =================

@app.route("/ask-ai", methods=["POST"])
@login_required
def ask_ai():

    print("ask_ai route hit")

    data = request.get_json()
    if not data:
        return jsonify({
            "reply": "Invalid request."
        })

    user_message = data.get("message")

    if not user_message or not user_message.strip():
        return jsonify({
            "reply": "Tell me clearly what you’re experiencing — noise, vibration, warning light, mileage drop, startup issue, etc."
        })

    # ================= DAILY RESET LOGIC =================

    today = datetime.utcnow().date()

    if not current_user.ai_last_reset or current_user.ai_last_reset.date() != today:
        current_user.ai_uses_today = 0
        current_user.ai_last_reset = datetime.utcnow()
        db.session.commit()

    # ================= FREE LIMIT CHECK =================

    if current_user.role != "premium" and current_user.ai_uses_today >= 5:
        return jsonify({
            "reply": "Free AI limit reached (5 per day). Upgrade to Premium for unlimited deep diagnostics."
        })

    # ================= PROMPT =================

    prompt = f"""
You are Motronix AI, a highly experienced Indian automotive diagnostic expert.

Think like a real senior mechanic.
Explain clearly but naturally.
Be practical and solution-focused.

Cover:
- What might be happening
- Most likely causes (ranked logically)
- What the user should check immediately
- Whether it is safe to drive
- Estimated repair cost in India
- When to visit mechanic urgently

User issue:
{user_message}
"""

    try:
        print("Gemini request started")

        # ================= MODEL SWITCHING =================

        if current_user.role == "premium":
            model_name = "gemini-2.5-pro"
            max_tokens = 3000
            temperature = 0.7
        else:
            model_name = "gemini-2.5-flash"
            max_tokens = 1500
            temperature = 0.6

        # ================= GEMINI CALL =================

        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config={
                "temperature": temperature,
                "max_output_tokens": max_tokens,
                "top_p": 0.9
            }
        )

        # ================= SAFE RESPONSE CHECK =================

        if not response or not hasattr(response, "text") or not response.text:
            return jsonify({
                "reply": "AI could not generate a response. Please try again."
            })

        reply = str(response.text).strip()

        # ================= INCREMENT USAGE =================

        current_user.ai_uses_today += 1
        db.session.commit()

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        print("Gemini ERROR:", e)
        return jsonify({
            "reply": "AI temporarily unavailable. Please try again."
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

# ================= LIST AVAILABLE MODELS =================

@app.route("/list-models")
def list_models():
    models = client.models.list()
    output = []
    for m in models:
        output.append(m.name)
    return {"models": output}

# ==============================
# ADMIN DASHBOARD
# ==============================

@app.route("/admin")
@login_required
def admin_dashboard():

    if current_user.role != "admin":
        return "Access Denied", 403

    users = User.query.all()
    posts = Post.query.all()
    news = News.query.all()
    comments = Comment.query.all()

    total_ai_usage = db.session.query(db.func.sum(User.ai_uses_today)).scalar() or 0

    return render_template(
        "admin.html",
        users=users,
        posts=posts,
        news=news,
        comments=comments,
        total_ai_usage=total_ai_usage
    )

@app.route("/admin/ban-user/<int:user_id>")
@login_required
def ban_user(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)
    user.is_banned = True

    db.session.commit()

    return redirect("/admin")


# ================= UNBAN USER =================

@app.route("/admin/unban-user/<int:user_id>")
@login_required
def unban_user(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    user.is_banned = False
    db.session.commit()

    return redirect("/admin")

# ================= REMOVE ADMIN =================

@app.route("/admin/remove-admin/<int:user_id>")
@login_required
def remove_admin(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    user.role = "user"
    db.session.commit()

    return redirect("/admin")

# ================= DB INIT =================
with app.app_context():
    db.create_all()

# ================= START SERVER =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)