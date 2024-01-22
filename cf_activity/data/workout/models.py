import uuid

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, \
    Integer, MetaData, String, Text, UUID, UniqueConstraint, text, Time
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from data import NAMING_CONVENTION
from data.datasets.models import (DictDifficultyOrm, DictExerciseOrm,
                                  DictWodTypeOrm, DictUnitOrm)
from data.user.models import User

SCHEMA_WORKOUT = 'workout'

metadata_workout = MetaData(schema=SCHEMA_WORKOUT,
                            naming_convention=NAMING_CONVENTION)
WorkoutBase = declarative_base(metadata=metadata_workout)


class WorkoutEntity(WorkoutBase):
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, comment='Идентификатор'
    )
    comment = Column(
        Text, nullable=True, comment='Комментарий'
    )


class Crossfitter(WorkoutBase):
    __tablename__ = 'dim_crossfitters'

    id_crossfitter = Column(BigInteger, ForeignKey(User.id), primary_key=True)
    birthday = Column(Date, nullable=True, comment='Дата рождения')
    height_sm = Column(Integer, nullable=True, comment='Рост в сантиметрах')
    gender = Column(String, nullable=True, comment='Пол')
    in_sport_since = Column(
        Integer, nullable=True, comment='С какого года в спорте'
    )


class WorkoutOfDay(WorkoutEntity):
    __tablename__ = 'dim_workouts'

    id_instructor = Column(
        BigInteger, ForeignKey(User.id), comment='идентификатор инструктора'
    )
    id_difficulty = Column(
        Integer,
        ForeignKey(DictDifficultyOrm.id), nullable=False,
        comment='сложность тренировки по мнению тренера'
    )
    wod_date = Column(
        Date, default=text('CURRENT_TIMESTAMP'),
        comment='дата проведения тренировки', nullable=False
    )
    wod_time = Column(
        Time, comment='время проведения тренировки', nullable=True
    )
    wod_requirement_level = Column(String, nullable=True)
    wod_place = Column(String, nullable=True)
    creation_date = Column(
        DateTime, server_default=text('CURRENT_TIMESTAMP'),
        comment='дата создания тренировки'
    )

    sets = relationship(
        'WodEntityOrm', back_populates='wod', lazy='selectin',
        order_by='WodEntityOrm.set_number'
    )


class WodEntityOrm(WorkoutEntity):
    __tablename__ = 'dim_wod_entities'

    id_wod = Column(
        UUID(as_uuid=True),
        ForeignKey(WorkoutOfDay.id, ondelete='RESTRICT'),
        nullable=False, comment=(
            'идентификатор тренировки, в которую входит комплекс')
    )
    id_wod_entity_parent = Column(
        UUID(as_uuid=True), ForeignKey('WodEntityOrm.id')
    )
    id_wod_type = Column(
        Integer, ForeignKey(DictWodTypeOrm.id, ondelete='RESTRICT'),
        nullable=True, comment='id названия комплекса'
    )
    id_exercise = Column(
        Integer, ForeignKey(DictExerciseOrm.id, ondelete='RESTRICT'),
        nullable=True, comment='id названия упражнения'
    )
    order_number = Column(
        Integer, nullable=True,
        comment='порядковый номер сущности'
    )
    variation = Column(
        Integer, nullable=True,
        comment='вариант исполнения (для разных кроссфиттеров)'
    )
    requirement_rounds_number = Column(
        Integer, nullable=True, comment='количество раундов'
    )
    requirement_duration_sec = Column(
        Integer, nullable=True, comment='длительность выполнения комплекса'
    )
    requirement_work_amount = Column(
        Integer, nullable=True, comment='объем нагрузки'
    )
    id_work_units = Column(
        Integer, ForeignKey(DictUnitOrm.id), nullable=True,
        comment='единицы измерения объема нагрузки'
    )
    requirement_reps_amount = Column(
        Integer, nullable=True, comment='количество повторений'
    )

    wod = relationship('WorkoutOfDay', back_populates='sets',
                       lazy='selectin')
    exercises = relationship(
        'Exercise', back_populates='set', lazy='selectin',
        order_by='Exercise.exercise_number'
    )
    results = relationship('SetResults')
    set_type = relationship(DictWodTypeOrm)

    __table_args__ = (
        UniqueConstraint('wod_id', 'set_number',
                         name='wod_set_num_uq'),
    )


class SetResults(WorkoutBase):
    __tablename__ = 'wod_superset_results'

    set_id = Column(
        UUID(as_uuid=True),
        ForeignKey(WodEntityOrm.id, ondelete='CASCADE'),
        primary_key=True, comment=(
            'идентификатор комплекса, для которого записывается результат')
    )
    duration_minutes = Column(
        Integer, nullable=True,
        comment='длительность выполнения'
    )
