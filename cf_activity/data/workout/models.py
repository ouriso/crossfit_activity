import uuid

from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, ForeignKey, \
    MetaData, UUID, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from data import NAMING_CONVENTION
from data.datasets.models import Difficulty, TrainingTypes
from data.user.models import User

SCHEMA_WORKOUT = 'workout'

metadata_workout = MetaData(schema=SCHEMA_WORKOUT,
                            naming_convention=NAMING_CONVENTION)
WorkoutBase = declarative_base(metadata=metadata_workout)


class WorkoutOfDay(WorkoutBase):
    __tablename__ = 'workout_of_day'

    rid = Column(
        'идентификатор тренировки', UUID(as_uuid=True),
        default=uuid.uuid4, primary_key=True
    )
    base_wod_rid = Column(
        UUID(as_uuid=True),
        ForeignKey('workout_of_day.rid', ondelete='RESTRICT'),
        nullable=True, comment='идентификатор тренировки от тренера'
    )
    base_wod = relationship('WorkoutOfDay', backref='child_wods')
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
        comment='дата проведения тренировки', auto_created=True
    )
    creation_date = Column(
        DateTime, server_default=text('CURRENT_TIMESTAMP'),
        comment='дата создания тренировки'
    )
    user = Column(
        BigInteger, ForeignKey(User.id, ondelete='CASCADE'),
    )
#
#
# class ExercisesSet(WorkoutBase):
#     rid = models.UUIDField(
#         'идентификатор комплекса', default=uuid.uuid4, primary_key=True
#     )
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='sets'
#     )
#     wod = models.ForeignKey(
#         WorkoutOfDay, on_delete=models.PROTECT, related_name='sets'
#     )
#     set_type = models.ForeignKey(
#         ExercisesSetType, on_delete=models.PROTECT
#     )
#     rounds = models.PositiveSmallIntegerField(
#         'количество раундов', null=True
#     )
#     duration_minutes = models.PositiveSmallIntegerField(
#         'длительность выполнения комплекса', null=True
#     )
#     set_number = models.PositiveSmallIntegerField(
#         'порядковый номер комплекса в тренировке'
#     )
#     comment = models.TextField('комментарий к комплексу', null=True,
#                                max_length=300)
#
#     class Meta:
#         ordering = ('set_number',)
#         verbose_name = 'комплекс'
#         verbose_name_plural = 'комплексы'
#         db_table = 'workout.exercises_set'
#         constraints = [
#             models.UniqueConstraint(fields=['wod', 'user', 'set_number'],
#                                     name='wod_user_set_num_uq')
#         ]
#
#
# class Exercise(WorkoutBase):
#     rid = models.UUIDField(
#         'идентификатор упражнения', default=uuid.uuid4, primary_key=True
#     )
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='exercises'
#     )
#     set = models.ForeignKey(
#         ExercisesSet, on_delete=models.PROTECT, related_name='exercises'
#     )
#     exercise_number = models.PositiveSmallIntegerField(
#         'порядковый номер упражнения в комплексе'
#     )
#     exercise_type = models.ForeignKey(
#         ExerciseType, on_delete=models.PROTECT
#     )
#     weight = models.PositiveSmallIntegerField(
#         'вес', null=True
#     )
#     reps_count = models.PositiveSmallIntegerField(
#         'количество повторений', null=True
#     )
#     rounds = models.PositiveSmallIntegerField(
#         'количество подходов', null=True
#     )
#     duration_minutes = models.PositiveSmallIntegerField(
#         'длительность выполнения', null=True
#     )
#     comment = models.TextField('комментарий к упражнению', null=True,
#                                max_length=300)
#
#     class Meta:
#         ordering = ('exercise_number',)
#         verbose_name = 'упражнение'
#         verbose_name_plural = 'упражнения'
#         db_table = 'workout.exercise'
#         constraints = [
#             models.UniqueConstraint(fields=['set', 'user', 'exercise_number'],
#                                     name='set_user_exercise_num_uq')
#         ]
#
#
# class ExerciseResults(WorkoutBase):
#     exercise = models.ForeignKey(
#         Exercise, on_delete=models.CASCADE, related_name='results'
#     )
#     round_number = models.PositiveSmallIntegerField(
#         'номер подхода'
#     )
#     weight = models.PositiveSmallIntegerField(
#         'вес', null=True
#     )
#     duration_minutes = models.PositiveSmallIntegerField(
#         'длительность выполнения', null=True
#     )
#     comment = models.TextField('комментарий к подходу', null=True,
#                                max_length=300)
#
#     class Meta:
#         ordering = ('round_number',)
#         verbose_name = 'подход'
#         verbose_name_plural = 'подходы'
#         db_table = 'workout.exercise_result'
#         constraints = [
#             models.UniqueConstraint(fields=['exercise', 'round_number'],
#                                     name='exercise_res_uq')
#         ]
#
