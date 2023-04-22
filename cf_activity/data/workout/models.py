import uuid

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, \
    Integer, MetaData, String, Text, UUID, UniqueConstraint, text
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


class WorkoutOfDay(WorkoutBase):
    __tablename__ = 'workout_of_day'

    rid = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, comment='идентификатор тренировки'
    )
    base_wod_rid = Column(
        UUID(as_uuid=True),
        ForeignKey('workout_of_day.rid', ondelete='RESTRICT'),
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


class ExercisesSet(WorkoutBase):
    __tablename__ = 'exercises_set'

    rid = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, comment='идентификатор комплекса'
    )
    wod_id = Column(
        UUID(as_uuid=True),
        ForeignKey('workout_of_day.rid', ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор тренировки, в которую входит комплекс')
    )
    set_number = Column(
        Integer, nullable=True,
        comment='порядковый номер комплекса в тренировке'
    )
    set_type_slug = Column(
        String, ForeignKey(ExercisesSetType.slug_name, ondelete='RESTRICT'),
        nullable=True, comment=(
            'slug названия комплекса')
    )
    rounds = Column(
        Integer, nullable=True, comment='количество раундов'
    )
    duration_minutes = Column(
        Integer, nullable=True, comment='длительность выполнения комплекса'
    )
    comment = Column(
        Text, nullable=True, comment='комментарий к комплексу'
    )

    __table_args__ = (
        UniqueConstraint('wod_id', 'set_number',
                         name='wod_set_num_uq'),
    )


class Exercise(WorkoutBase):
    __tablename__ = 'exercise'

    rid = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, comment='идентификатор упражнения'
    )
    set_id = Column(
        UUID(as_uuid=True),
        ForeignKey(ExercisesSet.rid, ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор комплекса, в который входит упражнение')
    )
    exercise_number = Column(
        Integer, nullable=True,
        comment='порядковый номер упражнения в комплексе'
    )
    exercise_type = Column(
        String, ForeignKey(ExerciseType.slug_name, ondelete='RESTRICT'),
        nullable=False, comment='slug типа тренировки'
    )
    rounds = Column(
        Integer, nullable=True, comment='количество раундов'
    )
    weight = Column(
        Integer, nullable=True,
        comment='вес снаряда / дополнительного груза'
    )
    reps_count = Column(
        Integer, nullable=True,
        comment='количество повторений'
    )
    duration_minutes = Column(
        Integer, nullable=True,
        comment='длительность выполнения'
    )
    comment = Column(
        Text, nullable=True, comment='комментарий к упражнению'
    )

    __table_args__ = (
        UniqueConstraint('set_id', 'exercise_number',
                         name='set_exercise_num_uq'),
    )


class SetResults(WorkoutBase):
    __tablename__ = 'set_result'

    set_id = Column(
        UUID(as_uuid=True),
        ForeignKey(ExercisesSet.rid, ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор комплекса, для которого записывается результат')
    )
    duration_minutes = Column(
        Integer, nullable=True,
        comment='длительность выполнения'
    )
    comment = Column(
        Text, nullable=True, comment='комментарий к результату комплекса'
    )

    __table_args__ = (
        UniqueConstraint('set_id', name='exercises_set_res_uq'),
    )


class ExerciseResults(WorkoutBase):
    __tablename__ = 'exercise_result'

    exercise_id = Column(
        UUID(as_uuid=True),
        ForeignKey(Exercise.rid, ondelete='CASCADE'),
        nullable=True, comment=(
            'идентификатор упражнения, для которого записывается результат')
    )
    round_number = Column(
        Integer, nullable=True, comment='номер подхода'
    )
    weight = Column(
        Integer, nullable=True,
        comment='вес снаряда / дополнительного груза'
    )
    reps_count = Column(
        Integer, nullable=True,
        comment='количество повторений'
    )
    duration_minutes = Column(
        Integer, nullable=True,
        comment='длительность выполнения'
    )
    comment = Column(
        Text, nullable=True, comment='комментарий к результату упражнения'
    )

    __table_args__ = (
        UniqueConstraint('exercise_id', 'round_number',
                         name='exercise_round_res_uq'),
    )
