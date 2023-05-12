from abc import ABC
from typing import Annotated, Type

from fastapi import Depends
from slugify import slugify
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import or_

from data import get_session
from data.datasets.models import BaseDatasetEntity, ExerciseType, \
    ExercisesSetType
from data.datasets.schemas import DatasetBase, ExerciseTypeSchema, \
    ExercisesSetTypeSchema


class BaseManager(ABC):
    orm_model: Type[BaseDatasetEntity] = None
    schema_model: Type[DatasetBase] = None

    @classmethod
    async def get_schema_by_id(cls, model_id: int, async_session: Annotated[
        AsyncSession, Depends(get_session)]) -> Type[orm_model]:
        obj = await cls.get_object_by_id(
            async_session, model_id)
        return obj

    @classmethod
    async def get_object_by_id(
            cls, async_session: AsyncSession, model_id: int
    ) -> orm_model:
        result = await async_session.execute(
            select(cls.orm_model).filter_by(id=model_id)
        )
        return result.scalar()

    @classmethod
    async def get_objects_by_name(
            cls, name: str, async_session: AsyncSession
    ) -> list[Type[orm_model]]:
        slug = slugify(name)
        result = await async_session.execute(
            select(cls.orm_model).filter(or_(
                cls.orm_model.name.startswith(name),
                cls.orm_model.slug_name.startswith(slug)
            ))
        )
        return list(result.scalars())

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
    ) -> Type[orm_model]:
        await async_session.execute(
            update(cls.orm_model).filter_by(id=model_id).values(**new_values)
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
    schema_model = ExerciseTypeSchema


class ExercisesSetTypeManager(BaseManager):
    orm_model = ExercisesSetType
    schema_model = ExercisesSetTypeSchema
