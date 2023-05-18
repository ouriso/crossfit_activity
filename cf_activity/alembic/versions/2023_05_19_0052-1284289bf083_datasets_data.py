"""Datasets data

Revision ID: 1284289bf083
Revises: e657aa2246c7
Create Date: 2023-05-19 00:52:16.691747

"""
from alembic import op

# revision identifiers, used by Alembic.
from data.datasets.models import ExerciseType, ExercisesSetType

revision = "1284289bf083"
down_revision = "e657aa2246c7"
branch_labels = None
depends_on = None

sets = [
    {"name": "К90 сек", "description": None},
    {"name": "AMREPS", "description": "AS MANY REPS AS POSSIBLE"},
    {"name": "CHIPPER", "description": None},
    {"name": "TABATA", "description": None},
    {"name": "21-15-9", "description": None},
    {"name": "EMOM", "description": "EVERY MINUTE ON MINUTE"},
    {"name": "DEATH BY", "description": None},
    {"name": "3x3", "description": None},
    {"name": "AMRAP", "description": "AS MANY ROUNDS AS POSSIBLE"},
    {"name": "AFAP", "description": "AS FAST AS POSSIBLE"},
]
exercises = [
    {"name": "HSPU", "description": None},
    {"name": "V-складка", "description": None},
    {"name": "Бег", "description": None},
    {"name": "Берпи", "description": None},
    {"name": "Берпи - через штангу", "description": None},
    {"name": "Велосипед", "description": None},
    {"name": "Выходы - на кольцах", "description": None},
    {"name": "Выходы - на перекладине", "description": None},
    {"name": "Выходы - строгие", "description": None},
    {"name": "Гантели - бицепс", "description": None},
    {"name": "Гантели - взятие", "description": None},
    {"name": "Гантели - выпады", "description": None},
    {"name": "Гантели - рывок", "description": None},
    {"name": "Гиперэкстензия", "description": None},
    {"name": "Гиря - махи", "description": None},
    {"name": "Гиря - становая", "description": None},
    {"name": "Гребля", "description": None},
    {"name": "Динамическая растяжка", "description": None},
    {"name": "Жим лежа", "description": None},
    {"name": "Канат", "description": None},
    {"name": "Мельница", "description": None},
    {"name": "Мяч", "description": None},
    {"name": "Отжимания", "description": None},
    {"name": "Отжимания - лопаточные", "description": None},
    {"name": "Отжимания - на кольцах", "description": None},
    {"name": "Подтягивания - австралийские", "description": None},
    {"name": "Подтягивания - киппинг", "description": None},
    {"name": "Подтягивания - лопаточные", "description": None},
    {"name": "Подтягивания - на кольцах", "description": None},
    {"name": "Подтягивания - с весом", "description": None},
    {"name": "Подтягивания - строгие", "description": None},
    {"name": "Пресс - v-складки", "description": None},
    {"name": "Пресс - на гиперэкстензии", "description": None},
    {"name": "Пресс - ноги к перекладине", "description": None},
    {"name": "Пресс - скручивания", "description": None},
    {"name": "Пресс - часики", "description": None},
    {"name": "Присед", "description": None},
    {"name": "Присед - фронтальный", "description": None},
    {"name": "Приседания", "description": None},
    {"name": "Приседания - пистолетом", "description": None},
    {"name": "Приседы - казацкие", "description": None},
    {"name": "Пружина в выпаде", "description": None},
    {"name": "Прыжки - на тумбу", "description": None},
    {"name": "Прыжки - через тумбу", "description": None},
    {"name": "Рывок", "description": None},
    {"name": "Скакалка", "description": None},
    {"name": "Скакалка - двойные прыжки", "description": None},
    {"name": "Скручивания в выпаде", "description": None},
    {"name": "Скручивания у стены", "description": None},
    {"name": "Собака-кошка", "description": None},
    {"name": "Становая тяга", "description": None},
    {"name": "Толчок", "description": None},
    {"name": "Трастер", "description": None},
    {"name": "Ходьба на руках", "description": None},
]


def upgrade() -> None:
    op.bulk_insert(ExercisesSetType.__table__, sets)
    op.bulk_insert(ExerciseType.__table__, exercises)


def downgrade() -> None:
    pass
