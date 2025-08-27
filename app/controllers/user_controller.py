from flask import render_template, request, redirect, url_for
from app.models.user import User
from app.db import db_session

class UserController:

    @staticmethod
    def list_users():
        users = db_session.query(User).all()
        return render_template('users.html', users=users)

    @staticmethod
    def create_user():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            new_user = User(name=name, email=email)
            db_session.add(new_user)
            db_session.commit()

            return redirect(url_for('list_users'))

        return render_template('create_user.html')

    @staticmethod
    def edit_user(user_id):
        user = db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return "Usuário não encontrado", 404

        if request.method == 'POST':
            user.name = request.form['name']
            user.email = request.form['email']
            db_session.commit()
            return redirect(url_for('list_users'))

        return render_template('edit_user.html', user=user)

    @staticmethod
    def delete_user(user_id):
        user = db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return "Usuário não encontrado", 404

        db_session.delete(user)
        db_session.commit()
        return redirect(url_for('list_users'))
from flask import render_template, request, redirect, url_for
from app.models.user import User
from app.db import db_session

class UserController:

    @staticmethod
    def list_users():
        users = db_session.query(User).all()
        return render_template('users.html', users=users)

    @staticmethod
    def create_user():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            new_user = User(name=name, email=email)
            db_session.add(new_user)
            db_session.commit()

            return redirect(url_for('list_users'))

        return render_template('create_user.html')

    @staticmethod
    def edit_user(user_id):
        user = db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return "Usuário não encontrado", 404

        if request.method == 'POST':
            user.name = request.form['name']
            user.email = request.form['email']
            db_session.commit()
            return redirect(url_for('list_users'))

        return render_template('edit_user.html', user=user)

    @staticmethod
    def delete_user(user_id):
        user = db_session.query(User).filter_by(id=user_id).first()

        if not user:
            return "Usuário não encontrado", 404

        db_session.delete(user)
        db_session.commit()
        return redirect(url_for('list_users'))
