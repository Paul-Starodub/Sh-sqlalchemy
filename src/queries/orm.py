from src.database import sync_engine, session_factory, async_session_factory, Base
from src.models import metadata, Worker


def create_tables():
    sync_engine.echo = True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():  # use sync session
    with session_factory() as session:
        worker_bobr = Worker(username="bobr999")
        worker_vovk = Worker(username="vovk777")
        # session.add(worker_bobr)
        # session.add(worker_vovk)
        session.add_all([worker_bobr, worker_vovk])
        session.commit()


async def insert_data():  # use async session
    async with async_session_factory() as session:
        worker_bobr = Worker(username="bobr333")
        worker_vovk = Worker(username="vovk444")
        session.add_all([worker_bobr, worker_vovk])
        await session.commit()
