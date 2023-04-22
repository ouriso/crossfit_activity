from os import getenv

from sqlalchemy import URL, create_engine

db_url = URL.create(
    getenv('DB_DRIVER', 'postgresql+psycopg'),
    username=getenv('DB_USER'),
    password=getenv('DB_PASS'),
    host=getenv('DB_HOST'),
    port=getenv('DB_PORT'),
    database=getenv('DB_NAME')
)

engine = create_engine(db_url)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
