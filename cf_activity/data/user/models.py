import enum

from sqlalchemy import BOOLEAN, BigInteger, Column, DateTime, Enum, Identity, \
    MetaData, String, text
from sqlalchemy.ext.declarative import declarative_base

from data import NAMING_CONVENTION

SCHEMA_USERS = 'users'

metadata_users = MetaData(schema=SCHEMA_USERS,
                          naming_convention=NAMING_CONVENTION)
UsersBase = declarative_base(metadata=metadata_users)


class UserRole(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'
    STAFF = 'staff'


class User(UsersBase):
    __tablename__ = 'user'

    id = Column(BigInteger, Identity(always=True), primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)  # TODO: encrypt this field
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    tg_user_id = Column(BigInteger, nullable=True, unique=True)
    is_active = Column(BOOLEAN, server_default=text('True'))
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    added = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated = Column(DateTime, nullable=True)
