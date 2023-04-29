"""empty message

Revision ID: 3ac070e5327e
Revises: aa8451b4f950
Create Date: 2023-04-30 00:49:23.832355

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "3ac070e5327e"
down_revision = "aa8451b4f950"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "exercise_type",
        sa.Column("id", sa.Integer(), sa.Identity(always=True), nullable=False),
        schema="datasets",
    )
    op.create_unique_constraint(
        op.f("uq_exercise_type_slug_name"),
        "exercise_type",
        ["slug_name"],
        schema="datasets",
    )
    op.add_column(
        "exercises_set_type",
        sa.Column("id", sa.Integer(), sa.Identity(always=True), nullable=False),
        schema="datasets",
    )
    op.create_unique_constraint(
        op.f("uq_exercises_set_type_slug_name"),
        "exercises_set_type",
        ["slug_name"],
        schema="datasets",
    )
    op.alter_column("exercise", column_name="rid", new_column_name="id",
                    schema="workout")
    op.add_column(
        "exercise",
        sa.Column(
            "exercise_type_id",
            sa.Integer(),
            nullable=False,
            comment="id типа тренировки",
        ),
        schema="workout",
    )
    op.drop_constraint(
        "fk_exercise_exercise_type_exercise_type",
        "exercise",
        schema="workout",
        type_="foreignkey",
    )
    op.drop_constraint("pk_exercise_type", "exercise_type",
                       "primary", "datasets")
    op.create_primary_key("pk_exercise_type", "exercise_type", ["id"],
                          "datasets")
    op.create_foreign_key(
        op.f("fk_exercise_exercise_type_id_exercise_type"),
        "exercise",
        "exercise_type",
        ["exercise_type_id"],
        ["id"],
        source_schema="workout",
        referent_schema="datasets",
        ondelete="RESTRICT",
    )
    op.drop_column("exercise", "exercise_type", schema="workout")
    op.alter_column("exercises_set", column_name="rid", new_column_name="id",
                    schema="workout")
    op.add_column(
        "exercises_set",
        sa.Column(
            "set_type_id", sa.Integer(), nullable=True,
            comment="id названия комплекса"
        ),
        schema="workout",
    )
    op.drop_constraint(
        "fk_exercises_set_set_type_slug_exercises_set_type",
        "exercises_set",
        schema="workout",
        type_="foreignkey",
    )
    op.drop_constraint("pk_exercises_set_type", "exercises_set_type",
                       "primary", "datasets")
    op.create_primary_key("pk_exercises_set_type", "exercises_set_type",
                          ["id"], "datasets")
    op.create_foreign_key(
        op.f("fk_exercises_set_set_type_id_exercises_set_type"),
        "exercises_set",
        "exercises_set_type",
        ["set_type_id"],
        ["id"],
        source_schema="workout",
        referent_schema="datasets",
        ondelete="RESTRICT",
    )
    op.drop_column("exercises_set", "set_type_slug", schema="workout")
    op.alter_column("workout_of_day", column_name="rid", new_column_name="id",
                    schema="workout")
    op.alter_column("workout_of_day", column_name="base_wod_rid",
                    new_column_name="base_wod_id", schema="workout")
