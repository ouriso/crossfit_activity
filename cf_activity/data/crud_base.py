from abc import ABC
from typing import Type, Union
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from data import SessionDep


class BaseManager(ABC):
    orm_model: Type[DeclarativeMeta] = None

    @classmethod
    async def get_object_by_id(
            cls, async_session: SessionDep, item_id: Union[int, UUID]
    ) -> orm_model:
        result_stmt = await async_session.execute(
            select(cls.orm_model).filter_by(id=item_id)
        )
        result = result_stmt.scalar()
        if not result:
            raise HTTPException(status_code=404, detail="Object not found")
        return result

    @classmethod
    async def get_objects_list(
            cls, async_session: AsyncSession
    ) -> list[Type[orm_model]]:
        result = await async_session.execute(
            select(cls.orm_model)
        )
        return list(result.scalars().all())

    @classmethod
    async def create_object(
            cls, async_session: AsyncSession, **values
    ) -> Type[orm_model]:
        new_instance = cls.orm_model(**values)
        async_session.add(new_instance)
        return new_instance

    @classmethod
    async def update_object(
            cls, async_session: AsyncSession,
            item_id: Union[int, UUID], **new_values
    ) -> Type[orm_model]:
        await async_session.execute(
            update(cls.orm_model).filter_by(id=item_id).values(**new_values)
        )

    @classmethod
    async def delete_object(
            cls, async_session: AsyncSession, item_id: Union[int, UUID]
    ) -> None:
        await async_session.execute(
            delete(cls.orm_model).where(id=item_id)
        )
