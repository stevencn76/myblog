from datetime import datetime

from flask_login import UserMixin

from routes import db, login_manager
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    fullname: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)

    def check_password_correction(self, attempted_password):
        return self.password == attempted_password
