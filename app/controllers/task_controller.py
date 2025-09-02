from flask import request, jsonify

# Banco de dados em memória
tasks = []
task_counter = 1


def get_tasks():
    """
    Lista todas as tarefas
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Lista de tarefas retornada com sucesso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              user_id:
                type: integer
              status:
                type: string
    """
    return jsonify(tasks), 200


def create_task():
    """
    Cria uma nova tarefa
    ---
    tags:
      - Tasks
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - user_id
          properties:
            title:
              type: string
            user_id:
              type: integer
    responses:
      201:
        description: Tarefa criada com sucesso
    """
    global task_counter

    data = request.get_json()
    title = data.get("title")
    user_id = data.get("user_id")

    if not title or not user_id:
        return jsonify({"error": "Campos 'title' e 'user_id' são obrigatórios"}), 400

    task = {
        "id": task_counter,
        "title": title,
        "user_id": user_id,
        "status": "pendente"
    }
    tasks.append(task)
    task_counter += 1

    return jsonify(task), 201


def update_task(task_id):
    """
    Atualiza uma tarefa existente
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            status:
              type: string
    responses:
      200:
        description: Tarefa atualizada com sucesso
      404:
        description: Tarefa não encontrada
    """
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["status"] = data.get("status", task["status"])
            return jsonify(task), 200

    return jsonify({"error": "Tarefa não encontrada"}), 404


def delete_task(task_id):
    """
    Exclui uma tarefa existente
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa excluída com sucesso
      404:
        description: Tarefa não encontrada
    """
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Tarefa excluída com sucesso"}), 200

    return jsonify({"error": "Tarefa não encontrada"}), 404
