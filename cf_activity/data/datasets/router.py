from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.datasets.crud import ExerciseTypeManager
from data.datasets.models import ExerciseType
from data.datasets.schemas import ExerciseTypeCreate, ExerciseTypeSchema, \
    ExerciseTypeUpdate

router_ds = APIRouter(
    prefix='/datasets',
)


@router_ds.get('/exercises/{item_id}', response_model=ExerciseTypeSchema)
async def get_exercise(
        exercise: ExerciseType = Depends(ExerciseTypeManager.get_object_by_id)
):
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


@router_ds.put('/exercises/{exercise_id}', response_model=ExerciseTypeSchema)
async def update_exercise(
        update_data: ExerciseTypeUpdate,
        exercise: ExerciseType = Depends(ExerciseTypeManager.get_schema_by_id),
        session: AsyncSession = Depends(get_session)
) -> ExerciseTypeSchema:
    await ExerciseTypeManager.update_object(
        session, exercise.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(exercise)
    return exercise
