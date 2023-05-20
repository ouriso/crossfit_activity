from datetime import date

from fastapi import HTTPException
from sqlalchemy import select

from data import SessionDep
from data.crud_base import BaseManager
from data.workout.models import Exercise, ExercisesSet, WorkoutOfDay


class ExerciseManager(BaseManager):
    orm_model = Exercise


class ExercisesSetManager(BaseManager):
    orm_model = ExercisesSet


class WODManager(BaseManager):
    orm_model = WorkoutOfDay

    @classmethod
    async def get_object_by_date(
            cls, async_session: SessionDep, action_date: date | str
    ) -> orm_model:
        result_stmt = await async_session.execute(
            select(cls.orm_model).filter_by(action_date=action_date)
        )
        result = result_stmt.scalar()
        if not result:
            raise HTTPException(status_code=404, detail="Object not found")
        return result
