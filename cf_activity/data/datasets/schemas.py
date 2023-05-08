from typing import Optional

from pydantic import BaseModel, validator
from slugify import slugify


class DatasetBase(BaseModel):
    name: str
    slug_name: str
    description: Optional[str]

    @classmethod
    @validator('slug_name', pre=True, always=True)
    def check_slug(cls, v, *, values, **kwargs):
        return v or slugify(values['name'])


class DatasetCreate(DatasetBase):
    pass


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True


class ExerciseTypeCreate(DatasetCreate):
    pass


class ExerciseTypeSchema(Dataset):
    pass


class ExercisesSetTypeCreate(DatasetCreate):
    pass


class ExercisesSetTypeSchema(Dataset):
    pass
