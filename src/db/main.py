from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from src.config import Config

# Async engine bound to the Postgres (Neon) database via asyncpg.
# Engine creation is lazy — no connection is opened until first use.
engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,  # log SQL statements to the console; set to False in production
    pool_pre_ping=True,  # verify connections before handing them out
)


async def init_db() -> None:
    """Standard database initialization: create all registered tables.

    Import your model modules here (e.g. ``from src.books import models``)
    so their tables are registered on ``SQLModel.metadata`` before ``create_all``.
    """
    async with engine.begin() as conn:
        from src.books.model import Book

        await conn.run_sync(SQLModel.metadata.create_all)
