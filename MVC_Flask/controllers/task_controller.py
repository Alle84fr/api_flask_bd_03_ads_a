from flask import render_template, request, redirect, url_for
from extensions import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        users = User.query.all()

        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            user_id = request.form["user_id"]

            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for("list_tasks"))

        return render_template("task_form.html", users=users)

    @staticmethod
    def update_task_status(task_id):
        task = Task.query.get_or_404(task_id)
        task.done = not task.done
        db.session.commit()
        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("list_tasks"))
