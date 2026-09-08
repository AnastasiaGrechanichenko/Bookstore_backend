import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

from models.user import User
from models.book import Book
from models.cart import CartItem
from models.favorite import Favorite
from models.order import Order, OrderItem
from models.login_session import LoginSession



db_url = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:142536@127.0.0.1/postgres")
engine = create_async_engine(db_url,echo = True)
AsyncSessionLocal = async_sessionmaker(engine,expire_on_commit=False)

sync_db_url = os.getenv("SYNC_DATABASE_URL","postgresql+psycopg2://postgres:142536@127.0.0.1/postgres")
sync_engine = create_engine(sync_db_url,echo=True)
SyncSessionLocal = sessionmaker(bind=sync_engine,expire_on_commit=False)



