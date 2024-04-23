from django.db import models
from uuid import uuid4
from datetime import date
from django.core.validators import MaxValueValidator

MAX_TEXT_LENGTH = 150
MAX_DURATION = 24*60
SCHEMA_NAME = 'musicians'


def current_year() -> int:
    return date.today().year


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    class Meta:
        # abstract says, that this is mixin, not database model
        abstract = True


class Musician(UUIDMixin):
    first_name = models.CharField(
        verbose_name='first name',
        max_length=MAX_TEXT_LENGTH
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=MAX_TEXT_LENGTH
    )
    birth_date = models.DateField(
        verbose_name='birth date',
        validators=(MaxValueValidator(date.today),),
        default=date.today
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."musicians"'
        verbose_name = 'musician'
        verbose_name_plural = 'musicians'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'


class Award(UUIDMixin):
    title = models.CharField(
        verbose_name='title',
        max_length=MAX_TEXT_LENGTH
    )
    year = models.PositiveIntegerField(
        verbose_name='year',
        default=current_year,
        validators=(MaxValueValidator(current_year),)
    )
    musician = models.ForeignKey(
        Musician,
        verbose_name='musician',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."awards"'
        unique_together = ('title', 'year')
        verbose_name = 'award'
        verbose_name_plural = 'awards'

    def __str__(self):
        return f'{self.title} {self.year}'


class Composition(UUIDMixin):
    title = models.CharField(
        verbose_name='title',
        max_length=MAX_TEXT_LENGTH
    )
    genre = models.CharField(
        verbose_name='genre',
        max_length=MAX_TEXT_LENGTH
    )
    duration = models.PositiveIntegerField(
        verbose_name='duration',
        validators=(MaxValueValidator(MAX_DURATION),)
    )
    musicians = models.ManyToManyField(
        Musician,
        verbose_name='musicians',
        through='MusicianComposition'
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."compositions"'
        verbose_name = 'composition'
        verbose_name_plural = 'compositions'

    def __str__(self):
        return f'{self.title} ({self.genre})'


class MusicianComposition(models.Model):
    musician = models.ForeignKey(
        Musician,
        verbose_name='musician',
        on_delete=models.CASCADE
    )
    composition = models.ForeignKey(
        Composition,
        verbose_name='composition',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."musicians_compositions"'
        unique_together = ('musician', 'composition')
        verbose_name = 'relationship musician-composition'
        verbose_name_plural = 'relationships musician-composition'

    def __str__(self):
        return f'{self.musician} - {self.composition}'
