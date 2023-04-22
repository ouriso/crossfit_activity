from enum import Enum

from slugify import slugify
from sqlalchemy import Column, MetaData, String, Text
from sqlalchemy.ext.declarative import declarative_base

from data import NAMING_CONVENTION

SCHEMA_DATASETS = 'datasets'

metadata_dataset = MetaData(schema=SCHEMA_DATASETS,
                            naming_convention=NAMING_CONVENTION)
DatasetBase = declarative_base(metadata=metadata_dataset)


class BaseDatasetEntity(DatasetBase):
    __abstract__ = True

    name = Column(String, nullable=False, unique=True)
    slug_name = Column(String, primary_key=True)
    description = Column(Text, nullable=True)

    @staticmethod
    def generate_slug_name(target, value, oldvalue, initiator):
        if value and (not target.slug_name or value != oldvalue):
            target.slug_name = slugify(value)


# slugify slug_name on creating new instance
event.listen(
    BaseDatasetEntity.name, 'set',
    BaseDatasetEntity.generate_slug_name, retval=False
)


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

