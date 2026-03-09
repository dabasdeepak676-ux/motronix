from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user

from models.models import db, Post, Comment, Vote
from werkzeug.utils import secure_filename
from flask import url_for
from models.models import db
import os

community_bp = Blueprint("community", __name__)


@community_bp.route("/community")
@login_required
def community():

    posts = Post.query.order_by(Post.id.desc()).all()

    return render_template(
        "community.html",
        posts=posts
    )


@community_bp.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():

    if request.method == "POST":

        title = request.form.get("title")
        content = request.form.get("content")

        if not title or not content:
            flash("Title and content required")
            return redirect("/create-post")

        post = Post(
            title=title,
            content=content,
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        flash("Post created successfully")

        return redirect("/community")

    return render_template("create_post.html")


@community_bp.route("/post/<int:post_id>")
def post_detail(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("post_detail.html", post=post)


@community_bp.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    if request.method == "POST":

        post.title = request.form["title"]
        post.content = request.form["content"]

        db.session.commit()

        return redirect(url_for("community.post_detail", post_id=post.id))

    return render_template("edit.html", post=post)


@community_bp.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    if post.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    db.session.delete(post)
    db.session.commit()

    return redirect("/community")


@community_bp.route("/add_comment/<int:post_id>", methods=["POST"])
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

    return redirect(url_for("community.post_detail", post_id=post_id))


@community_bp.route("/upvote/<int:post_id>")
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

# ================= EDIT COMMENT =================

@community_bp.route("/comment/<int:comment_id>/edit", methods=["GET", "POST"])
@login_required
def edit_comment(comment_id):

    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    if request.method == "POST":
        comment.content = request.form["content"]
        db.session.commit()

        return redirect(url_for("community.post_detail", post_id=comment.post_id))

    return render_template("edit_comment.html", comment=comment)


# ================= DELETE COMMENT =================

@community_bp.route("/comment/<int:comment_id>/delete", methods=["POST"])
@login_required
def delete_comment(comment_id):

    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != current_user.id and current_user.role != "admin":
        return "Unauthorized"

    post_id = comment.post_id

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for("community.post_detail", post_id=post_id))