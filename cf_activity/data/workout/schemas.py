import uuid
from datetime import date

from pydantic import BaseModel, Field

from data.datasets.models import Difficulty, TrainingTypes
from data.datasets.schemas import Dataset


class ExerciseBase(BaseModel):
    set_id: uuid.UUID
    exercise_number: int
    exercise_type_id: int
    rounds: int | None
    work: int | None
    unit_of_work: str | None
    reps_count: int | None
    duration_seconds: int | None
    comment: str | None


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseUpdate(ExerciseBase):
    set_id: uuid.UUID | None
    exercise_number: int | None
    exercise_type_id: int | None


class Exercise(ExerciseBase):
    id: uuid.UUID
    exercise_type: Dataset

    class Config:
        orm_mode = True


class ExercisesSetBase(BaseModel):
    wod_id: uuid.UUID
    set_number: int
    set_type_id: int
    rounds: int | None
    duration_minutes: int | None
    comment: str | None


class ExercisesSetCreate(ExerciseBase):
    pass


class ExercisesSetUpdate(ExerciseBase):
    wod_id: uuid.UUID | None
    set_number: int | None
    set_type_id: int | None


class ExercisesSet(ExerciseBase):
    id: uuid.UUID
    set_type: Dataset
    exercises: list[Exercise] | None

    class Config:
        orm_mode = True


class WorkoutOfDayBase(BaseModel):
    base_wod_id: uuid.UUID | None
    training_type: TrainingTypes = TrainingTypes.ENDURANCE
    difficulty: Difficulty = Difficulty.NORMAL
    action_date: date = date.today()
    comment: str | None


class WorkoutOfDayCreate(WorkoutOfDayBase):
    pass


class WorkoutOfDayUpdate(WorkoutOfDayBase):
    training_type: TrainingTypes | None
    difficulty: Difficulty | None
    action_date: date | None


class WorkoutOfDay(WorkoutOfDayBase):
    id: uuid.UUID
    user_id: int = Field(..., exclude=True)
    sets: list[ExercisesSet] | None

    class Config:
        orm_mode = True
