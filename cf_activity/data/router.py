from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.datasets.crud import ExerciseTypeManager
from data.datasets.schemas import ExerciseTypeCreate, ExerciseTypeSchema

router_ds = APIRouter(
    prefix='/datasets',
)


@router_ds.get('/exercises/{exercise_id}', response_model=ExerciseTypeSchema)
async def get_exercise(
        exercise_id: int, session: AsyncSession = Depends(get_session)
):
    exercise = await ExerciseTypeManager.get_object_by_id(session, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


@router_ds.get('/exercises/', response_model=list[ExerciseTypeSchema])
async def get_exercises_list(
        session: AsyncSession = Depends(get_session), name: str = None
):
    if name:
        exercises = await ExerciseTypeManager.get_objects_by_name(
            name, session
        )
    else:
        exercises = await ExerciseTypeManager.get_objects_list(session)
    return exercises


@router_ds.post('/exercises/', response_model=ExerciseTypeSchema)
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
