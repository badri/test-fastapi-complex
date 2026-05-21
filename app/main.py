import os
import asyncpg
from fastapi import FastAPI

app = FastAPI()
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/app")

@app.get("/")
def index():
    return {"message": "hello from fastapi"}

@app.get("/health")
async def health():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.close()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
