import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from .database import engine, Base
from .models import *
from .controller import auth, home
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine  

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        if isinstance(engine, AsyncEngine):
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logging.info("Database tables created successfully (async)")
        else:
            Base.metadata.create_all(bind=engine)
            logging.info("Database tables created successfully (sync - consider switching engine)")
    except Exception as e:
        logging.error(f"Database initialization failed: {e}")
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="YHMQIcn6QFUn5y96B6fBSHnq6J7SZDKr9LYUTGJ6gZ3T2c")

app.include_router(home.router)
app.include_router(auth.router)