# Ateliê Online - Cadastro de Serviços

Este projeto é uma aplicação em **Flask** estruturada no padrão **MVC**
que permite o cadastro e a listagem de serviços de um ateliê.\
Inclui integração com banco de dados **MySQL** e documentação interativa
com **Swagger (Flasgger)**.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Python 3
-   Flask
-   Flask-SQLAlchemy
-   Flasgger (Swagger UI)
-   MySQL (ou SQLite para testes)
-   HTML, CSS, JavaScript

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    atelie_online/
    │── app.py                # Arquivo principal
    │── config.py             # Configuração da aplicação
    │
    ├── controllers/          # Controladores (rotas e lógica da API)
    │   └── servico_controller.py
    │
    ├── models/               # Modelos do banco de dados
    │   └── servico_model.py
    │
    ├── static/               # Arquivos estáticos (CSS, JS)
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── script.js
    │
    ├── templates/            # Templates HTML (caso queira visualizar no browser)
    │   ├── base.html
    │   ├── cadastro_servico.html
    │   └── lista_servicos.html

------------------------------------------------------------------------

## 📌 Endpoints da API (Swagger)

A documentação interativa pode ser acessada em:

    http://127.0.0.1:5000/apidocs/

### Principais Rotas

-   `GET /servicos` → Lista todos os serviços
-   `POST /servicos` → Cria um novo serviço
-   `PUT /servicos/<id>` → Atualiza um serviço
-   `DELETE /servicos/<id>` → Remove um serviço

------------------------------------------------------------------------

## Feito por:

1. Alessandra Furlanetto Rigonatti - 2401151
2. Enzo Pelakoski Cavinato - 2400911
3. Guilherme de Freitas Fracasso - 2400916
4. Matheus Barros Ferreira - 2401102
5. Rafaela Wohlers Rodrigues - 2404142

## Diagrama ER:

+-------------+        +----------------+        +-----------------+
|  cliente    |1------<|  agendamento   |>------1|   servico       |
+-------------+        +----------------+        +-----------------+
| id_cliente  |        | id_agendamento |        | id_servico      |
| nome        |        | id_cliente     |        | nome            |
| email       |        | id_servico     |        | preco           |
+-------------+        +----------------+        +-----------------+
                               |
                               v
                        +------------------+
                        |   funcionario    |
                        +------------------+
                        | id_funcionario   |
                        | nome             |
                        | cargo            |
                        +------------------+
                               ^
                               |
                         +--------------+
                         | servico_func.|
                         +--------------+
                         | id_servico   |
                         | id_funcion.  |
                         +--------------+
