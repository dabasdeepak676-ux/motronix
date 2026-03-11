from flask import Blueprint, render_template, redirect, flash
from flask_login import login_required, current_user
from models.models import db, User, Post, Comment, News, WebsiteVisit

admin_bp = Blueprint("admin", __name__)


# ================= ADMIN DASHBOARD =================

@admin_bp.route("/admin")
@login_required
def admin_dashboard():

     
    if current_user.role != "admin":
        return "Access Denied", 403

    users = User.query.all()
    posts = Post.query.all()
    comments = Comment.query.all()
    news = News.query.all()

    total_ai_usage = db.session.query(db.func.sum(User.ai_uses_today)).scalar() or 0
    visit_count = WebsiteVisit.query.count()
    return render_template(
    "admin.html",
    users=users,
    posts=posts,
    comments=comments,
    news=news,
    total_ai_usage=total_ai_usage,
    visit_count=visit_count
)


# ================= DELETE USER =================

@admin_bp.route("/admin/delete-user/<int:user_id>")
@login_required
def delete_user(user_id):

    if current_user.role != "admin":
        return "Access Denied"

    user = User.query.get_or_404(user_id)

    # admin खुद को delete नहीं कर सकता
    if user.id == current_user.id:
        flash("You cannot delete yourself")
        return redirect("/admin")

    # पहले user के posts delete
    Post.query.filter_by(user_id=user.id).delete()

    # user के comments delete
    Comment.query.filter_by(user_id=user.id).delete()

    # अब user delete
    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully")

    return redirect("/admin")


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