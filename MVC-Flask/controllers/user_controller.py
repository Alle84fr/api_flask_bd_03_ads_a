from flask import render_template, request, redirect, url_for
from extensions import db
from models.user import User

class UserController:

    @staticmethod
    def list_users():
        users = User.query.all()
        return render_template("users.html", users=users)

    @staticmethod
    def create_user():
        if request.method == "POST":
            name = request.form["name"]
            email = request.form["email"]

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("list_users"))

        return render_template("user_form.html")

    @staticmethod
    def edit_user(user_id):
        user = User.query.get_or_404(user_id)

        if request.method == "POST":
            user.name = request.form["name"]
            user.email = request.form["email"]
            db.session.commit()
            return redirect(url_for("list_users"))

        return render_template("user_form.html", user=user)

    @staticmethod
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("list_users"))
