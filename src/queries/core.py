from sqlalchemy import text, insert
from src.database import sync_engine, async_engine, session_factory
from src.models import metadata, workers_table


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")


async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")


def create_tables():
    sync_engine.echo = False
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES ('bobr'), ('vovk');"""
        # conn.execute(text(stmt))
        stmt = insert(workers_table).values([{"username": "bobr11"}, {"username": "vovk11"}])  # query builder
        conn.execute(stmt)
        conn.commit()
