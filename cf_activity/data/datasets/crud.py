from abc import ABC
from typing import Type

from slugify import slugify
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import or_

from data.datasets.models import BaseDatasetEntity, ExerciseType, \
    ExercisesSetType


class BaseManager(ABC):
    orm_model: Type[BaseDatasetEntity] = None

    @classmethod
    async def get_object_by_id(
            cls, async_session: AsyncSession, model_id: int
    ) -> orm_model:
        result = await async_session.execute(
            select(cls.orm_model).filter_by(id=model_id)
        )
        return result.scalar().first()

    @classmethod
    async def get_objects_by_name(
            cls, async_session: AsyncSession, name: str = None
    ) -> list[Type[orm_model]]:
        slug = slugify(name)
        result = await async_session.execute(
            select(cls.orm_model).filter(or_(
                cls.orm_model.name == name,
                cls.orm_model.slug_name == slug
            ))
        )
        return list(result.all())

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
            model_id: int, **new_values
    ) -> None:
        await async_session.execute(
            update(cls.orm_model).where(id=model_id).values(**new_values)
        )

    @classmethod
    async def delete_object(
            cls, async_session: AsyncSession, model_id: int
    ) -> None:
        await async_session.execute(
            delete(cls.orm_model).where(id=model_id)
        )


class ExerciseTypeManager(BaseManager):
    orm_model = ExerciseType


class ExercisesSetTypeManager(BaseManager):
    orm_model = ExercisesSetType
