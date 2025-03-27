import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import engine, Base

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Database initialization failed: {e}")

    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", tags=["Health Check"])
async def read_root():
    return {"message": "FastAPI with PostgreSQL is connected"}
