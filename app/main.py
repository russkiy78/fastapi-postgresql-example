from fastapi import FastAPI
from app.db import init_db
from app.routes import example

app = FastAPI(title="FastAPI + PostgreSQL Template")


# DB init
@app.on_event("startup")
async def startup():
    init_db()


# routes
app.include_router(example.router)
