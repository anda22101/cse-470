from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse



DATABASE_URL = "postgresql+asyncpg://anda:andalib@localhost:2210/quizwizz"




engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit = False, autoflush = False)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session
