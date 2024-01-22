from sqlalchemy import Column, Identity, Integer, MetaData, String, Text
from sqlalchemy.ext.declarative import declarative_base

from data import NAMING_CONVENTION

SCHEMA_DATASETS = 'datasets'

metadata_dataset = MetaData(schema=SCHEMA_DATASETS,
                            naming_convention=NAMING_CONVENTION)
DatasetBase = declarative_base(metadata=metadata_dataset)


class BaseDatasetEntity(DatasetBase):
    __abstract__ = True

    id = Column(Integer, Identity(always=True), primary_key=True)
    name = Column(
        String, nullable=False, unique=True, comment='Название сущности'
    )
    description = Column(Text, nullable=True, comment='Описание сущности')


class DictExerciseOrm(BaseDatasetEntity):
    """Type of exercise."""
    __tablename__ = 'dict_exercises'


class DictWodTypeOrm(BaseDatasetEntity):
    """Type of set of exercises."""
    __tablename__ = 'dict_wod_types'


class DictDifficultyOrm(BaseDatasetEntity):
    """Training difficulty."""
    __tablename__ = 'dict_difficulties'


class DictUnitOrm(BaseDatasetEntity):
    """Work units."""
    __tablename__ = 'dict_units'

    symbol = Column(
        String, nullable=True, comment='Символ для единицы измерения'
    )
