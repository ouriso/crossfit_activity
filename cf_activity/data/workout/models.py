import uuid

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, \
    Integer, MetaData, String, Text, UUID, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from data import NAMING_CONVENTION
from data.datasets.models import Difficulty, ExerciseType, ExercisesSetType, \
    TrainingTypes
from data.user.models import User

SCHEMA_WORKOUT = 'workout'

metadata_workout = MetaData(schema=SCHEMA_WORKOUT,
                            naming_convention=NAMING_CONVENTION)
WorkoutBase = declarative_base(metadata=metadata_workout)


class HasComment:
    comment = Column(
        Text, nullable=True, comment='Комментарий'
    )


class WorkoutEntity(WorkoutBase, HasComment):
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, comment='Идентификатор'
    )


class WorkoutOfDay(WorkoutEntity):
    __tablename__ = 'workout_of_day'

    base_wod_id = Column(
        UUID(as_uuid=True),
        ForeignKey('workout_of_day.id', ondelete='RESTRICT'),
        nullable=True, comment='идентификатор тренировки от тренера'
    )
    training_type = Column(
        Enum(TrainingTypes),
        default=TrainingTypes.ENDURANCE, nullable=False,
        comment='тип тренировки'
    )
    difficulty = Column(
        Enum(Difficulty),
        default=Difficulty.NORMAL, nullable=False,
        comment='субъективная сложность тренировки'
    )
    action_date = Column(
        Date, default=text('CURRENT_TIMESTAMP'),
        comment='дата проведения тренировки', nullable=False
    )
    creation_date = Column(
        DateTime, server_default=text('CURRENT_TIMESTAMP'),
        comment='дата создания тренировки'
    )
    user_id = Column(
        BigInteger, ForeignKey(User.id, ondelete='CASCADE'),
    )

    base_wod = relationship('WorkoutOfDay', backref='child_wods')
    user = relationship('User', backref='wods')
    sets = relationship('ExercisesSet', backref='wod')


class ExercisesSet(WorkoutEntity):
    __tablename__ = 'exercises_set'

    wod_id = Column(
        UUID(as_uuid=True),
        ForeignKey(WorkoutOfDay.id, ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор тренировки, в которую входит комплекс')
    )
    set_number = Column(
        Integer, nullable=True,
        comment='порядковый номер комплекса в тренировке'
    )
    set_type_id = Column(
        Integer, ForeignKey(ExercisesSetType.id, ondelete='RESTRICT'),
        nullable=True, comment=(
            'id названия комплекса')
    )
    rounds = Column(
        Integer, nullable=True, comment='количество раундов'
    )
    duration_minutes = Column(
        Integer, nullable=True, comment='длительность выполнения комплекса'
    )

    exercises = relationship('Exercise', backref='set')
    results = relationship('SetResults', backref='set')
    set_type = relationship(ExercisesSetType)

    __table_args__ = (
        UniqueConstraint('wod_id', 'set_number',
                         name='wod_set_num_uq'),
    )


class Exercise(WorkoutEntity):
    __tablename__ = 'exercise'

    set_id = Column(
        UUID(as_uuid=True),
        ForeignKey(ExercisesSet.id, ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор комплекса, в который входит упражнение')
    )
    exercise_number = Column(
        Integer, nullable=True,
        comment='порядковый номер упражнения в комплексе'
    )
    exercise_type_id = Column(
        Integer, ForeignKey(ExerciseType.id, ondelete='RESTRICT'),
        nullable=False, comment='id типа тренировки'
    )
    rounds = Column(
        Integer, nullable=True, comment='количество раундов'
    )
    work = Column(
        Integer, nullable=True,
        comment='нагрузка: вес / калории / мощность'
    )
    unit_of_work = Column(
        String(15), nullable=True, default='кг.',
        comment='единицы измерения нагрузки'
    )
    reps_count = Column(
        Integer, nullable=True,
        comment='количество повторений'
    )
    duration_seconds = Column(
        Integer, nullable=True,
        comment='длительность выполнения, сек'
    )

    results = relationship('ExerciseResults', backref='exercise')
    exercise_type = relationship(ExerciseType)

    __table_args__ = (
        UniqueConstraint('set_id', 'exercise_number',
                         name='set_exercise_num_uq'),
    )


class SetResults(WorkoutBase, HasComment):
    __tablename__ = 'set_result'

    set_id = Column(
        UUID(as_uuid=True),
        ForeignKey(ExercisesSet.id, ondelete='CASCADE'),
        primary_key=True, comment=(
            'идентификатор комплекса, для которого записывается результат')
    )
    duration_minutes = Column(
        Integer, nullable=True,
        comment='длительность выполнения'
    )


class ExerciseResults(WorkoutBase, HasComment):
    __tablename__ = 'exercise_result'

    exercise_id = Column(
        UUID(as_uuid=True),
        ForeignKey(Exercise.id, ondelete='CASCADE'),
        primary_key=True, comment=(
            'идентификатор упражнения, для которого записывается результат')
    )
    weights = Column(
        ARRAY(Integer), nullable=True,
        comment='список весов снаряда / дополнительного груза в каждом подходе'
    )
    reps_counts = Column(
        ARRAY(Integer), nullable=True,
        comment='список количества повторений в каждом подходе'
    )
    duration_minutes = Column(
        ARRAY(Integer), nullable=True,
        comment='список длительности выполнения в каждом подходе'
    )
