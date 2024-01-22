from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.datasets.crud import DictExerciseManager, DictSupersetManager
from data.datasets.models import DictExerciseOrm, DictWodTypeOrm
from data.datasets.schemas import DatasetCreate, Dataset, DatasetUpdate

router_ds = APIRouter(
    prefix='/datasets',
)


@router_ds.get('/exercises/{item_id}', response_model=Dataset)
async def get_exercise(
        exercise: DictExerciseOrm = Depends(
            DictExerciseManager.get_object_by_id
        )
):
    return exercise


@router_ds.get('/exercises/', response_model=list[Dataset])
async def get_exercises_list(
        session: AsyncSession = Depends(get_session), name: str = None
):
    if name:
        exercises = await DictExerciseManager.get_objects_by_name(
            name, session
        )
    else:
        exercises = await DictExerciseManager.get_objects_list(session)
    return exercises


@router_ds.post('/exercises/', response_model=Dataset)
async def create_exercise(
        exercise: DatasetCreate,
        session: AsyncSession = Depends(get_session)
):
    new_exercise = await DictExerciseManager.create_object(
        session, **exercise.model_dump()
    )
    await session.commit()
    await session.refresh(new_exercise)
    return new_exercise


@router_ds.put('/exercises/{item_id}', response_model=Dataset)
async def update_exercise(
        update_data: DatasetUpdate,
        exercise: DictExerciseOrm = Depends(
            DictExerciseManager.get_object_by_id
        ),
        session: AsyncSession = Depends(get_session)
) -> Dataset:
    await DictExerciseManager.update_object(
        session, exercise.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(exercise)
    return exercise


@router_ds.get('/sets/{item_id}', response_model=Dataset)
async def get_exercises_set(
        exercises_set: DictWodTypeOrm = Depends(
            DictSupersetManager.get_object_by_id)
):
    return exercises_set


@router_ds.get('/sets/', response_model=list[Dataset])
async def get_exercises_sets_list(
        session: AsyncSession = Depends(get_session), name: str = None
):
    if name:
        exercises = await DictSupersetManager.get_objects_by_name(
            name, session
        )
    else:
        exercises = await DictSupersetManager.get_objects_list(session)
    return exercises


@router_ds.post('/sets/', response_model=Dataset)
async def create_exercises_set(
        exercise: DatasetCreate,
        session: AsyncSession = Depends(get_session)
):
    new_exercise = await DictSupersetManager.create_object(
        session, **exercise.dict()
    )
    await session.commit()
    await session.refresh(new_exercise)
    return new_exercise


@router_ds.put('/sets/{item_id}', response_model=Dataset)
async def update_exercise(
        update_data: DatasetUpdate,
        exercise: DictExerciseOrm = Depends(
            DictSupersetManager.get_object_by_id),
        session: AsyncSession = Depends(get_session)
) -> Dataset:
    await DictExerciseManager.update_object(
        session, exercise.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(exercise)
    return exercise
