from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.datasets.crud import ExerciseTypeManager
from data.datasets.schemas import ExerciseTypeCreate, ExerciseTypeSchema

router_wod = APIRouter()


@router_wod.get('/exercises/', response_model=list[ExerciseTypeSchema])
async def get_exercises(session: AsyncSession = Depends(get_session)):
    exercises = await ExerciseTypeManager.get_objects_list(session)
    # return [ExerciseTypeSchema.from_orm(exc) for exc in exercises]
    return exercises


@router_wod.post('/exercises/', response_model=ExerciseTypeSchema)
async def create_exercise(
        exercise: ExerciseTypeCreate,
        session: AsyncSession = Depends(get_session)
):
    new_exercise = await ExerciseTypeManager.create_object(
        session, **exercise.dict()
    )
    await session.commit()
    await session.refresh(new_exercise)
    return new_exercise
