from dotenv import load_dotenv
load_dotenv()
from ai_engine.diagnostic_engine import diagnose_vehicle
from failure_database import FAILURE_DATABASE
from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from models.models import db, User, Post, Comment, Vote, News, DiagnosticLearning, Car
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from routes.auth_routes import auth_bp
from flask_wtf import CSRFProtect
from services.email_service import send_email
from routes.community_routes import community_bp
from routes.ai_routes import ai_bp
from routes.admin_routes import admin_bp

import os
from PIL import Image


from collections import defaultdict
from google import genai
import re
from datetime import datetime, timedelta


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
app.register_blueprint(auth_bp)
app.register_blueprint(community_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(admin_bp)

print("Motronix server booting...")

# ================= FILE SIZE LIMIT =================
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

# ================= ALLOWED IMAGE TYPES =================

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
def compress_image(image_path):

    try:

        img = Image.open(image_path)

        img = img.convert("RGB")

        img.save(
            image_path,
            format="JPEG",
            quality=70,
            optimize=True
        )

    except Exception as e:

        print("Image compression error:", e)

def safe_image_check(file_path):

    try:
        img = Image.open(file_path)
        img.verify()

        if img.format.lower() not in ["jpeg","png","webp"]:
            return False

        return True

    except:
        return False
ADMIN_EMAILS = [
"dabasdeepak676@gmail.com",
"riteshsingh1609@gmail.com",
"channelspeed16@gmail.com",
"mechanicalbull@gmail.com"
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
@app.route("/test-email")
def test_email():

    send_email(
        mail,
        "YOUR_EMAIL@gmail.com",
        "Motronix Test Email",
        "SMTP working!"
    )

    return "Email sent"
database_url = os.environ.get("DATABASE_URL")

# Render PostgreSQL compatibility fix
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url or "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

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

# POST IMAGE UPLOAD FOLDER

POST_IMAGE_UPLOAD = "static/post_images"
app.config["POST_IMAGE_UPLOAD"] = POST_IMAGE_UPLOAD



if not os.path.exists(POST_IMAGE_UPLOAD):
    os.makedirs(POST_IMAGE_UPLOAD)


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):

    return "." in filename and \
    filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

if not os.path.exists(POST_IMAGE_UPLOAD):
    os.makedirs(POST_IMAGE_UPLOAD)

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
login_manager.login_view = "auth.login"

from email.header import Header

        # ================= VIDEOS =================

@app.route("/videos")
def videos():

    youtube_videos = [
        "https://www.youtube.com/embed/VIDEO_ID_1",
        "https://www.youtube.com/embed/VIDEO_ID_2",
        "https://www.youtube.com/embed/VIDEO_ID_3"
    ]

    instagram_posts = [
        "https://www.instagram.com/p/POST_ID_1/embed",
        "https://www.instagram.com/p/POST_ID_2/embed"
    ]

    return render_template(
        "videos.html",
        youtube_videos=youtube_videos,
        instagram_posts=instagram_posts
    )

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
# ================= SET DEFAULT CAR =================

@app.route("/set-default-car/<int:car_id>")
@login_required
def set_default_car(car_id):

    # remove old default
    cars = Car.query.filter_by(owner_id=current_user.id).all()

    for c in cars:
        c.is_default = False

    # set new default
    car = Car.query.get_or_404(car_id)

    if car.owner_id != current_user.id:
        return "Unauthorized"

    car.is_default = True

    db.session.commit()

    return redirect("/garage")

# ================= GARAGE =================

@app.route("/garage")
@login_required
def garage():

    cars = Car.query.filter_by(owner_id=current_user.id).all()

    return render_template("garage.html", cars=cars)


# ================= AI DIAGNOSE =================

# ================= AI DIAGNOSE =================

@app.route("/diagnose", methods=["GET", "POST"])
@login_required
def diagnose():

    cars = Car.query.filter_by(owner_id=current_user.id).all()

    if request.method == "POST":

        problem = request.form.get("problem")
        car_id = request.form.get("car_id")

        # Get selected car
        car = Car.query.get(car_id)

        if not car:
            flash("Please select a car.")
            return redirect("/diagnose")

        answers = {}

        for key in request.form:
            if key not in ["problem", "car_id"]:
                answers[key] = request.form.get(key)

        results, questions = diagnose_vehicle(problem, answers)

        if results:

            learning = DiagnosticLearning(
                problem_text=problem,
                predicted_issue=results[0]["issue"],
                confidence=results[0]["confidence"]
            )

            db.session.add(learning)
            db.session.commit()

        return render_template(
            "diagnosis_result.html",
            results=results,
            questions=questions,
            problem=problem,
            car=car
        )

    return render_template("diagnose.html", cars=cars)
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


# ================= SYMPTOM SUGGESTION =================

@app.route("/symptom-suggest")
def symptom_suggest():

    query = request.args.get("q","").lower().strip()

    if not query:
        return jsonify({"suggestions":[]})

    suggestions = []

    for failure in FAILURE_DATABASE:

        # problem match
        problem = failure.get("problem","").lower()

        if query in problem:
            suggestions.append(problem)

        # match individual words
        for word in problem.split():

            if query in word:
                suggestions.append(problem)

        # search symptoms
        for symptom in failure.get("symptoms",[]):

            s = symptom.lower()

            if query in s:
                suggestions.append(s)

            for w in s.split():

                if query in w:
                    suggestions.append(s)

    # remove duplicates
    suggestions = list(set(suggestions))

    # limit suggestions
    suggestions = suggestions[:10]

    return jsonify({"suggestions":suggestions})

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

            image_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )

        news = News(
            title=request.form["title"],
            content=request.form["content"],
            image=filename
        )

        db.session.add(news)
        db.session.commit()

        return redirect("/news")

    return render_template("create_news.html")


import requests
# ================= EDIT NEWS =================

@app.route("/admin/news/edit/<int:news_id>", methods=["GET","POST"])
@login_required
def edit_news(news_id):

    if current_user.role != "admin":
        return "Access Denied"

    news = News.query.get_or_404(news_id)

    if request.method == "POST":

        news.title = request.form["title"]
        news.content = request.form["content"]

        image_file = request.files.get("image")

        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            news.image = filename

        db.session.commit()

        return redirect("/news")

    return render_template("edit_news.html", news=news)
# ================= DELETE NEWS =================

@app.route("/admin/news/delete/<int:news_id>")
@login_required
def delete_news(news_id):

    if current_user.role != "admin":
        return "Access Denied"

    news = News.query.get_or_404(news_id)

    db.session.delete(news)
    db.session.commit()

    return redirect("/news")
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
    mail,
    email,
    "Reset your Motronix password",
    f"Click this link to reset your password:\n\n{reset_link}"
)

            flash("Reset link sent to your email.")
        else:
            flash("Email not found.")

    return render_template("forgot_password.html")


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

    return redirect(url_for("community.post_detail", post_id=post_id))

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

    return redirect(url_for("auth.login"))

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

        return redirect(url_for("auth.login"))

    return render_template("reset_password.html")

# ================= LIST AVAILABLE MODELS =================

@app.route("/list-models")
def list_models():
    models = client.models.list()
    output = []
    for m in models:
        output.append(m.name)
    return {"models": output}


# ================= DB INIT =================
 
# ================= START SERVER =================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5001))

    print("Starting Motronix server on port:", port)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
