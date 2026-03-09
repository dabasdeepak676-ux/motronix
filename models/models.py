from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

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

    reset_token = db.Column(db.String(200))
    reset_token_expiry = db.Column(db.DateTime)

    verification_token = db.Column(db.String(200))
    verification_token_expiry = db.Column(db.DateTime)

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

    image = db.Column(db.String(200))

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

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class DiagnosticLearning(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    problem_text = db.Column(db.Text)

    predicted_issue = db.Column(db.String(200))

    confidence = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Car(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)

    fuel_type = db.Column(db.String(50))
    mileage = db.Column(db.Integer)

    is_default = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    owner = db.relationship("User", backref="cars")