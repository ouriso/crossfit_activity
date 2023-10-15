"""Datasets data

Revision ID: 1284289bf083
Revises: e657aa2246c7
Create Date: 2023-05-19 00:52:16.691747

"""
from alembic import op
from slugify import slugify
from sqlalchemy import String
from sqlalchemy.sql import column, table

# revision identifiers, used by Alembic.

revision = "1284289bf083"
down_revision = "e657aa2246c7"
branch_labels = None
depends_on = None

sets = [
    {"name": "К90 сек", "slug_name": slugify("К90 сек"), "description": None},
    {"name": "AMREPS", "slug_name": slugify("AMREPS"), "description": "AS MANY REPS AS POSSIBLE"},
    {"name": "CHIPPER", "slug_name": slugify("CHIPPER"), "description": None},
    {"name": "TABATA", "slug_name": slugify("TABATA"), "description": None},
    {"name": "21-15-9", "slug_name": slugify("21-15-9"), "description": None},
    {"name": "EMOM", "slug_name": slugify("EMOM"), "description": "EVERY MINUTE ON MINUTE"},
    {"name": "DEATH BY", "slug_name": slugify("DEATH BY"), "description": None},
    {"name": "3x3", "slug_name": slugify("3x3"), "description": None},
    {"name": "AMRAP", "slug_name": slugify("AMRAP"), "description": "AS MANY ROUNDS AS POSSIBLE"},
    {"name": "AFAP", "slug_name": slugify("AFAP"), "description": "AS FAST AS POSSIBLE"},
]
exercises = [
    {"name": "HSPU", "slug_name": slugify("HSPU"), "description": None},
    {"name": "V-складка", "slug_name": slugify("V-складка"), "description": None},
    {"name": "Бег", "slug_name": slugify("Бег"), "description": None},
    {"name": "Берпи", "slug_name": slugify("Берпи"), "description": None},
    {"name": "Берпи - через штангу", "slug_name": slugify("Берпи - через штангу"), "description": None},
    {"name": "Велосипед", "slug_name": slugify("Велосипед"), "description": None},
    {"name": "Выходы - на кольцах", "slug_name": slugify("Выходы - на кольцах"), "description": None},
    {"name": "Выходы - на перекладине", "slug_name": slugify("Выходы - на перекладине"), "description": None},
    {"name": "Выходы - строгие", "slug_name": slugify("Выходы - строгие"), "description": None},
    {"name": "Гантели - бицепс", "slug_name": slugify("Гантели - бицепс"), "description": None},
    {"name": "Гантели - взятие", "slug_name": slugify("Гантели - взятие"), "description": None},
    {"name": "Гантели - выпады", "slug_name": slugify("Гантели - выпады"), "description": None},
    {"name": "Гантели - рывок", "slug_name": slugify("Гантели - рывок"), "description": None},
    {"name": "Гиперэкстензия", "slug_name": slugify("Гиперэкстензия"), "description": None},
    {"name": "Гиря - махи", "slug_name": slugify("Гиря - махи"), "description": None},
    {"name": "Гиря - становая", "slug_name": slugify("Гиря - становая"), "description": None},
    {"name": "Гребля", "slug_name": slugify("Гребля"), "description": None},
    {"name": "Динамическая растяжка", "slug_name": slugify("Динамическая растяжка"), "description": None},
    {"name": "Жим лежа", "slug_name": slugify("Жим лежа"), "description": None},
    {"name": "Канат", "slug_name": slugify("Канат"), "description": None},
    {"name": "Мельница", "slug_name": slugify("Мельница"), "description": None},
    {"name": "Мяч", "slug_name": slugify("Мяч"), "description": None},
    {"name": "Отжимания", "slug_name": slugify("Отжимания"), "description": None},
    {"name": "Отжимания - лопаточные", "slug_name": slugify("Отжимания - лопаточные"), "description": None},
    {"name": "Отжимания - на кольцах", "slug_name": slugify("Отжимания - на кольцах"), "description": None},
    {"name": "Подтягивания - австралийские", "slug_name": slugify("Подтягивания - австралийские"), "description": None},
    {"name": "Подтягивания - киппинг", "slug_name": slugify("Подтягивания - киппинг"), "description": None},
    {"name": "Подтягивания - лопаточные", "slug_name": slugify("Подтягивания - лопаточные"), "description": None},
    {"name": "Подтягивания - на кольцах", "slug_name": slugify("Подтягивания - на кольцах"), "description": None},
    {"name": "Подтягивания - с весом", "slug_name": slugify("Подтягивания - с весом"), "description": None},
    {"name": "Подтягивания - строгие", "slug_name": slugify("Подтягивания - строгие"), "description": None},
    {"name": "Пресс - v-складки", "slug_name": slugify("Пресс - v-складки"), "description": None},
    {"name": "Пресс - на гиперэкстензии", "slug_name": slugify("Пресс - на гиперэкстензии"), "description": None},
    {"name": "Пресс - ноги к перекладине", "slug_name": slugify("Пресс - ноги к перекладине"), "description": None},
    {"name": "Пресс - скручивания", "slug_name": slugify("Пресс - скручивания"), "description": None},
    {"name": "Пресс - часики", "slug_name": slugify("Пресс - часики"), "description": None},
    {"name": "Присед", "slug_name": slugify("Присед"), "description": None},
    {"name": "Присед - фронтальный", "slug_name": slugify("Присед - фронтальный"), "description": None},
    {"name": "Приседания", "slug_name": slugify("Приседания"), "description": None},
    {"name": "Приседания - пистолетом", "slug_name": slugify("Приседания - пистолетом"), "description": None},
    {"name": "Приседы - казацкие", "slug_name": slugify("Приседы - казацкие"), "description": None},
    {"name": "Пружина в выпаде", "slug_name": slugify("Пружина в выпаде"), "description": None},
    {"name": "Прыжки - на тумбу", "slug_name": slugify("Прыжки - на тумбу"), "description": None},
    {"name": "Прыжки - через тумбу", "slug_name": slugify("Прыжки - через тумбу"), "description": None},
    {"name": "Рывок", "slug_name": slugify("Рывок"), "description": None},
    {"name": "Скакалка", "slug_name": slugify("Скакалка"), "description": None},
    {"name": "Скакалка - двойные прыжки", "slug_name": slugify("Скакалка - двойные прыжки"), "description": None},
    {"name": "Скручивания в выпаде", "slug_name": slugify("Скручивания в выпаде"), "description": None},
    {"name": "Скручивания у стены", "slug_name": slugify("Скручивания у стены"), "description": None},
    {"name": "Собака-кошка", "slug_name": slugify("Собака-кошка"), "description": None},
    {"name": "Становая тяга", "slug_name": slugify("Становая тяга"), "description": None},
    {"name": "Толчок", "slug_name": slugify("Толчок"), "description": None},
    {"name": "Трастер", "slug_name": slugify("Трастер"), "description": None},
    {"name": "Ходьба на руках", "slug_name": slugify("Ходьба на руках"), "description": None},
]


def upgrade() -> None:
    exercises_set_type = table(
        'exercises_set_type',
        column('name', String), column('slug_name', String),
        column('description', String),
        schema='datasets'
    )
    exercise_type = table(
        'exercise_type',
        column('name', String), column('slug_name', String),
        column('description', String),
        schema='datasets'
    )

    op.bulk_insert(exercises_set_type, sets)
    op.bulk_insert(exercise_type, exercises)


def downgrade() -> None:
    pass
