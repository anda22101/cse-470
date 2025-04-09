from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

DATABASE_URL = "postgresql+asyncpg://anda:andalib@localhost:2210/quizwizz"  
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session