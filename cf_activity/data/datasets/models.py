from enum import Enum

from sqlalchemy import Column, Identity, Integer, MetaData, String, Text
from sqlalchemy.ext.declarative import declarative_base

from data import NAMING_CONVENTION
from data.datasets.utils import generate_slug_name

SCHEMA_DATASETS = 'datasets'

metadata_dataset = MetaData(schema=SCHEMA_DATASETS,
                            naming_convention=NAMING_CONVENTION)
DatasetBase = declarative_base(metadata=metadata_dataset)


class BaseDatasetEntity(DatasetBase):
    __abstract__ = True

    id = Column(Integer, Identity(always=True), primary_key=True)
    name = Column(String, nullable=False, unique=True)
    slug_name = Column(String, nullable=False, unique=True,
                       default=generate_slug_name, onupdate=generate_slug_name)
    description = Column(Text, nullable=True)


class ExerciseType(BaseDatasetEntity):
    """Type of exercise."""
    __tablename__ = 'exercise_type'


class ExercisesSetType(BaseDatasetEntity):
    """Type of set of exercises."""
    __tablename__ = 'exercises_set_type'


class Difficulty(Enum):
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'
    HELL = 'hell'


class TrainingTypes(Enum):
    POWER = 'power'
    ENDURANCE = 'endurance'
    FULL_BODY = 'full_body'
    GYM = 'gymnastics'
