from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from data import NAMING_CONVENTION

SCHEMA_DATASETS = 'datasets'

metadata_dataset = MetaData(schema=SCHEMA_DATASETS,
                            naming_convention=NAMING_CONVENTION)
DatasetBase = declarative_base(metadata=metadata_dataset)
