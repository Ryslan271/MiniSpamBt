import sqlalchemy as sa
from sqlalchemy_file import FileField
from .db_session import SqlAlchemyBase


class Messages(SqlAlchemyBase):
    __tablename__ = 'Messages'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    senderId = sa.Column(sa.Integer, nullable=False)
    text = sa.Column(sa.String, nullable=False)
    file = sa.Column(FileField, nullable=True)


class UserIDs(SqlAlchemyBase):
    __tablename__ = 'UserIDs'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    senderId = sa.Column(sa.Integer, nullable=False)
    ListIds = sa.Column(sa.String, nullable=False)