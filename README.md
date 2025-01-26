# fastapi-postgresql-example
FastAPI +  Postgresql RESTful API Template


## Run the project
Make sure PostgreSQL is running and create a database:

`CREATE DATABASE db_name;`

Start the server:

`uvicorn app.main:app --reload`

The API will be available at: http://127.0.0.1:8000

You can open the Swagger documentation at: http://127.0.0.1:8000/docs.

This template is easily extended to add new models, routes or dependencies.
