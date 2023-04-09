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
