from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, func
import datetime 

class Base(DeclarativeBase):
    pass

class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]


class PushupsORM(Base):
    __tablename__ = "pushups"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    number: Mapped[int]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())