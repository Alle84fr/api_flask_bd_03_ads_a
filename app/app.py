from flask import Flask, request
from flasgger import Swagger
from app.controllers.task_controller import TaskController
from app.db import init_db

app = Flask(__name__)
swagger = Swagger(app)


app.add_url_rule('/tasks', 'list_tasks', TaskController.list_tasks)
app.add_url_rule('/tasks/new', 'create_task', TaskController.create_task, methods=['GET', 'POST'])
app.add_url_rule('/tasks/update/<int:task_id>', 'update_task_status', TaskController.update_task_status, methods=['POST'])
app.add_url_rule('/tasks/delete/<int:task_id>', 'delete_task', TaskController.delete_task, methods=['POST'])

@app.before_request
def override_method():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method == 'DELETE':
            request.environ['REQUEST_METHOD'] = method

if __name__ == "__main__":
    app.run(debug=True)
