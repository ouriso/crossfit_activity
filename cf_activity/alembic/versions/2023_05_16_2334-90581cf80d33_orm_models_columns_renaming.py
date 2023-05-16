"""ORM models columns renaming

Revision ID: 90581cf80d33
Revises: 3ac070e5327e
Create Date: 2023-05-16 23:34:34.682010

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '90581cf80d33'
down_revision = '3ac070e5327e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('exercise', 'weight',
                    comment='нагрузка: вес / калории / мощность',
                    new_column_name='work', schema='workout')
    op.alter_column('exercise', 'duration_minutes',
                    comment='длительность выполнения, сек',
                    new_column_name='duration_seconds', schema='workout')
    op.add_column('exercise',
                  sa.Column('unit_of_work', sa.String(length=15), nullable=True,
                            comment='единицы измерения нагрузки'),
                  schema='workout')
    op.add_column('workout_of_day',
                  sa.Column('comment', sa.Text(), nullable=True,
                            comment='комментарий к тренировке'),
                  schema='workout')


def downgrade() -> None:
    op.drop_column('workout_of_day', 'comment', schema='workout')
    op.drop_column('exercise', 'unit_of_work', schema='workout')
    op.alter_column('exercise', 'work',
                    comment='вес снаряда / дополнительного груза',
                    new_column_name='weight', schema='workout')
    op.alter_column('exercise', 'duration_seconds',
                    comment='длительность выполнения, мин',
                    new_column_name='duration_minutes', schema='workout')
