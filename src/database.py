import asyncio
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

from src.config import settings

sync_engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,  # count of connections to database
    # max_overflow=10,  # additional connections
)

# with sync_engine.begin() as conn:  #  begin makes commit instead of connection
#     res = conn.execute(text("SELECT VERSION()"))
#     print(res)
#
# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     # print(res)
#     # print(res.all())
#     # print(res.first())
#     # print(res.one())
#     # print(res.one_or_none())
#     print(f"{res.all()=}")

async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg,
    echo=True,
    # pool_size=5,  # count of connections to database
    # max_overflow=10,  # additional connections
)
#
#
# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.all()=}")
#
#
# asyncio.run(get_123())

# with Session(sync_engine) as session:  # requires passing engine
#     session.execute(text("SELECT VERSION()"))

# session = sessionmaker(sync_engine)
#
# with session() as session:  # without engine
#     session.execute(text("SELECT VERSION()"))

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

# async with async_session() as session:  # requires wrapping in async with
#     await session.execute(text("SELECT VERSION()"))


class Base(DeclarativeBase):
    pass
