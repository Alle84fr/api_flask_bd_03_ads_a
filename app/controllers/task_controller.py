from flask import render_template, request, redirect, url_for
from app.models.task import Task
from app.models.user import User
from app.db import db_session

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = db_session.query(Task).all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form.get('description')
            user_id = request.form['user_id']

            new_task = Task(
                title=title,
                description=description,
                status='Pendente',
                user_id=user_id
            )
            db_session.add(new_task)
            db_session.commit()
            return redirect(url_for('list_tasks'))

        users = db_session.query(User).all()
        return render_template("create_task.html", users=users)

    @staticmethod
    def update_task_status(task_id):
        task = db_session.query(Task).filter_by(id=task_id).first()
        if task:
            task.status = 'Concluída' if task.status == 'Pendente' else 'Pendente'
            db_session.commit()
        return redirect(url_for('list_tasks'))

    @staticmethod
    def delete_task(task_id):
        task = db_session.query(Task).filter_by(id=task_id).first()
        if task:
            db_session.delete(task)
            db_session.commit()
        return redirect(url_for('list_tasks'))
