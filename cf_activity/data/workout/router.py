from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data import get_session
from data.workout.crud import WODManager
from data.workout import models
from data.workout import schemas

router_wod = APIRouter(
    prefix='/wod'
)


@router_wod.get('/{item_id}', response_model=schemas.WorkoutOfDay)
async def get_wod(
        wod: models.WorkoutOfDay = Depends(
            WODManager.get_object_by_id)
):
    return wod


@router_wod.get('/', response_model=list[schemas.WorkoutOfDay])
async def get_wod_list(
        session: AsyncSession = Depends(get_session), action_date: str = None
):
    if action_date:
        wods = await WODManager.get_object_by_date(
            session, action_date
        )
    else:
        wods = await WODManager.get_objects_list(session)
    return wods


@router_wod.post('/', response_model=schemas.WorkoutOfDay)
async def create_wod(
        wod: schemas.WorkoutOfDayCreate,
        user_id=1,
        session: AsyncSession = Depends(get_session)
):
    new_wod = await WODManager.create_object(
        session, **wod.dict(), user_id=user_id
    )
    await session.commit()
    await session.refresh(new_wod)
    return new_wod


@router_wod.put('/{item_id}', response_model=schemas.WorkoutOfDay)
async def update_exercise(
        update_data: schemas.WorkoutOfDayUpdate,
        wod: models.WorkoutOfDay = Depends(
            WODManager.get_object_by_id),
        session: AsyncSession = Depends(get_session)
) -> schemas.WorkoutOfDay:
    await WODManager.update_object(
        session, wod.id, **update_data.dict(exclude_unset=True)
    )
    await session.commit()
    await session.refresh(wod)
    return wod
