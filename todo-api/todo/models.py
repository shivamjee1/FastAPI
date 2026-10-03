from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import mapped_column, Mapped

from .database import Base

class todo(Base):
    __tablename__= "Todos"
    id : Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    title : Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    discription : Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    completed : Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )