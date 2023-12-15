from datetime import datetime

from routes import db
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column


class Article(db.Model):
    __tablename__ = 'articles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    __content: Mapped[bytes] = mapped_column(BLOB, name="content", nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True, server_default=func.now())

    @property
    def content(self):
        return self.__content.decode('utf-8')

    @content.setter
    def content(self, content_value: str):
        self.__content = content_value.encode()
