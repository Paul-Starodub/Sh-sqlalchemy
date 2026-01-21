from sqlalchemy import Table, Column, Integer, String, MetaData
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()

workers_table = Table("workers", metadata, Column("id", Integer, primary_key=True), Column("username", String))  # imperative style


class Worker(Base):  # declarative style
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
