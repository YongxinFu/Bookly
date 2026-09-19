from datetime import datetime
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column
from sqlmodel import Field, SQLModel


class Book(SQLModel, table=True):
    __tablename__ = "book"
    id: UUID = Field(
        sa_column=Column(
            pg.UUID,
            default=uuid4,
            primary_key=True,
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    create_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP,
            default=datetime.now,
            onupdate=datetime.now,
        )
    )
