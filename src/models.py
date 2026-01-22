from datetime import datetime
from typing import Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func
from src.database import Base, str_200
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

metadata = MetaData()

# custom types
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime | None, mapped_column(onupdate=func.now())]

workers_table = Table(
    "workers", metadata, Column("id", Integer, primary_key=True), Column("username", String)
)  # imperative style


class Worker(Base):  # declarative style
    __tablename__ = "workers"
    id: Mapped[intpk]
    username: Mapped[str]
    resumes: Mapped[list["Resume"]] = relationship(back_populates="worker")


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class Resume(Base):
    __tablename__ = "resumes"
    id: Mapped[intpk]
    title: Mapped[str_200]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    worker: Mapped["Worker"] = relationship(back_populates="resumes")
