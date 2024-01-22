from typing import Annotated, Type

from fastapi import Depends
from slugify import slugify
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import or_

from data import get_session
from data.crud_base import BaseManager
from data.datasets.models import BaseDatasetEntity, DictExerciseOrm, \
    DictWodTypeOrm

SessionDep = Annotated[AsyncSession, Depends(get_session)]


class DatasetManager(BaseManager):
    orm_model: Type[BaseDatasetEntity] = None

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


class DictExerciseManager(DatasetManager):
    orm_model = DictExerciseOrm


class DictSupersetManager(DatasetManager):
    orm_model = DictWodTypeOrm
