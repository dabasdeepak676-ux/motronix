from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from models.models import db, User, Post, Comment, News

# ================= BLUEPRINT =================

admin_bp = Blueprint("admin", __name__)


# ================= ADMIN DASHBOARD =================

@admin_bp.route("/admin")
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


# ================= BAN USER =================

@admin_bp.route("/admin/ban-user/<int:user_id>")
@login_required
def ban_user(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    user.is_banned = True
    db.session.commit()

    return redirect("/admin")


# ================= UNBAN USER =================

@admin_bp.route("/admin/unban-user/<int:user_id>")
@login_required
def unban_user(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    user.is_banned = False
    db.session.commit()

    return redirect("/admin")


# ================= REMOVE ADMIN =================

@admin_bp.route("/admin/remove-admin/<int:user_id>")
@login_required
def remove_admin(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    user.role = "user"
    db.session.commit()

    return redirect("/admin")