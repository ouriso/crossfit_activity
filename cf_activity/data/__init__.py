from os import getenv

from sqlalchemy import URL, create_engine

db_url = URL.create(
    'postgresql+psycopg3',
    username=getenv('PSG_USER'),
    password=getenv('PSG_PASS'),
    host=getenv('PSG_HOST'),
    port=getenv('PSG_PORT'),
    database=getenv('PSG_DB')
)

engine = create_engine(db_url)

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
