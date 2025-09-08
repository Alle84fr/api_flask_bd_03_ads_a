from flask import Flask, redirect, url_for
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///to_do_list.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev"

    db.init_app(app)

    from models.user import User
    from models.task import Task
    from controllers.user_controller import UserController
    from controllers.task_controller import TaskController

    # Rotas Usuários
    app.add_url_rule("/users", view_func=UserController.list_users, methods=["GET"], endpoint="list_users")
    app.add_url_rule("/users/new", view_func=UserController.create_user, methods=["GET", "POST"], endpoint="create_user")
    app.add_url_rule("/users/edit/<int:user_id>", view_func=UserController.edit_user, methods=["GET", "POST"], endpoint="edit_user")
    app.add_url_rule("/users/delete/<int:user_id>", view_func=UserController.delete_user, methods=["POST"], endpoint="delete_user")

    # Rotas Tarefas
    app.add_url_rule("/tasks", view_func=TaskController.list_tasks, methods=["GET"], endpoint="list_tasks")
    app.add_url_rule("/tasks/new", view_func=TaskController.create_task, methods=["GET", "POST"], endpoint="create_task")
    app.add_url_rule("/tasks/update/<int:task_id>", view_func=TaskController.update_task_status, methods=["POST"], endpoint="update_task_status")
    app.add_url_rule("/tasks/delete/<int:task_id>", view_func=TaskController.delete_task, methods=["POST"], endpoint="delete_task")

    # Página inicial
    @app.route("/")
    def index():
        return redirect(url_for("list_tasks"))

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
