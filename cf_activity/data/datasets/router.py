from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.datasets.crud import ExerciseTypeManager, ExercisesSetTypeManager
from data.datasets.models import ExerciseType, ExercisesSetType
from data.datasets.schemas import DatasetCreate, Dataset, DatasetUpdate

router_ds = APIRouter(
    prefix='/datasets',
)


@router_ds.get('/exercises/{item_id}', response_model=Dataset)
async def get_exercise(
        exercise: ExerciseType = Depends(ExerciseTypeManager.get_object_by_id)
):
    return exercise


@router_ds.get('/exercises/', response_model=list[Dataset])
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


@router_ds.post('/exercises/', response_model=Dataset)
async def create_exercise(
        exercise: DatasetCreate,
        session: AsyncSession = Depends(get_session)
):
    new_exercise = await ExerciseTypeManager.create_object(
        session, **exercise.dict()
    )
    await session.commit()
    await session.refresh(new_exercise)
    return new_exercise


@router_ds.put('/exercises/{item_id}', response_model=Dataset)
async def update_exercise(
        update_data: DatasetUpdate,
        exercise: ExerciseType = Depends(ExerciseTypeManager.get_object_by_id),
        session: AsyncSession = Depends(get_session)
) -> Dataset:
    await ExerciseTypeManager.update_object(
        session, exercise.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(exercise)
    return exercise


@router_ds.get('/sets/{item_id}', response_model=Dataset)
async def get_exercises_set(
        exercises_set: ExercisesSetType = Depends(
            ExercisesSetTypeManager.get_object_by_id)
):
    return exercises_set


@router_ds.get('/sets/', response_model=list[Dataset])
async def get_exercises_sets_list(
        session: AsyncSession = Depends(get_session), name: str = None
):
    if name:
        exercises = await ExercisesSetTypeManager.get_objects_by_name(
            name, session
        )
    else:
        exercises = await ExercisesSetTypeManager.get_objects_list(session)
    return exercises


@router_ds.post('/sets/', response_model=Dataset)
async def create_exercises_set(
        exercise: DatasetCreate,
        session: AsyncSession = Depends(get_session)
):
    new_exercise = await ExercisesSetTypeManager.create_object(
        session, **exercise.dict()
    )
    await session.commit()
    await session.refresh(new_exercise)
    return new_exercise


@router_ds.put('/sets/{item_id}', response_model=Dataset)
async def update_exercise(
        update_data: DatasetUpdate,
        exercise: ExerciseType = Depends(
            ExercisesSetTypeManager.get_object_by_id),
        session: AsyncSession = Depends(get_session)
) -> Dataset:
    await ExerciseTypeManager.update_object(
        session, exercise.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(exercise)
    return exercise
