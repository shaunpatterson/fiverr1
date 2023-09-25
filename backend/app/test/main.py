import os
import datetime
import uuid
from typing import List, Optional

from sqlalchemy import DateTime, ForeignKeyConstraint, Integer, JSON, LargeBinary, PrimaryKeyConstraint, Text, \
    UniqueConstraint, text, Boolean, Uuid, Double
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import Boolean, DateTime, Double, ForeignKeyConstraint, Integer, JSON, LargeBinary, PrimaryKeyConstraint, Text, UniqueConstraint, Uuid, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

class Base(DeclarativeBase):
    pass

class Test(Base):
    __tablename__ = 'test'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='test_pk'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('now()'))


SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_DATABASE_URI)

engine = create_engine(str(SQLALCHEMY_DATABASE_URI), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI(title="Test")


@app.get("/api/test")
async def get():
    print("Creating tables")
    Base.metadata.create_all(engine)

    db = SessionLocal()
    t = Test(name="This is a test")
    db.add(t)
    db.commit()
    db.refresh(t)
    return dict(id=t.id, test=t.name)


