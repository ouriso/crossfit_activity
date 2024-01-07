from typing import Optional

from pydantic import BaseModel, field_validator
from slugify import slugify


class DatasetBase(BaseModel):
    name: str
    slug_name: Optional[str]
    description: Optional[str]

    @classmethod
    @field_validator('slug_name', 'name')
    def check_slug(cls, v, *, values):
        if not values.get('name') and not v:
            return None
        return v or slugify(values['name'])


class DatasetCreate(DatasetBase):
    pass


class DatasetUpdate(DatasetBase):
    name: Optional[str]


class Dataset(DatasetBase):
    id: int

    class Config:
        orm_mode = True
