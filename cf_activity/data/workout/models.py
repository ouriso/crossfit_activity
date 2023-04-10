from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from data import NAMING_CONVENTION

SCHEMA_WORKOUT = 'workout'

metadata_workout = MetaData(schema=SCHEMA_WORKOUT,
                            naming_convention=NAMING_CONVENTION)
WorkoutBase = declarative_base(metadata=metadata_workout)
