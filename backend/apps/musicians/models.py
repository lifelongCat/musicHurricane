from datetime import date
from uuid import uuid4

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_TEXT_LENGTH = 150
MAX_DURATION = 24*60
SCHEMA_NAME = 'musicians'


def current_year() -> int:
    return date.today().year


class UUIDMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    class Meta:
        # abstract says, that this is mixin, not database model
        abstract = True


class Musician(UUIDMixin):
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=MAX_TEXT_LENGTH,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=MAX_TEXT_LENGTH,
    )
    birth_date = models.DateField(
        verbose_name=_('birth date'),
        validators=(MaxValueValidator(date.today),),
        default=date.today,
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."musicians"'
        verbose_name = _('musician')
        verbose_name_plural = _('musicians')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date.strftime("%d.%m.%Y")}'


class Award(UUIDMixin):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=MAX_TEXT_LENGTH,
    )
    year = models.PositiveIntegerField(
        verbose_name=_('year'),
        default=current_year,
        validators=(MaxValueValidator(current_year),),
    )
    musician = models.ForeignKey(
        Musician,
        verbose_name=_('musician'),
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."awards"'
        unique_together = ('title', 'year')
        verbose_name = _('award')
        verbose_name_plural = _('awards')

    def __str__(self):
        return f'{self.title} {self.year}'


class Composition(UUIDMixin):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=MAX_TEXT_LENGTH,
    )
    genre = models.CharField(
        verbose_name=_('genre'),
        max_length=MAX_TEXT_LENGTH,
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('duration'),
        validators=(MaxValueValidator(MAX_DURATION),),
    )
    musicians = models.ManyToManyField(
        Musician,
        verbose_name=_('musicians'),
        through='MusicianComposition',
    )
    audio_file = models.FileField(
        verbose_name=_('audio file'),
    )

    def save(self, *args, **kwargs):
        if not self.id:
            saved_file = self.audio_file
            self.audio_file = None  # noqa: WPS601, shadowed class attribute
            super().save(*args, **kwargs)
            self.audio_file = saved_file  # noqa: WPS601, shadowed class attribute
        # self.file.name = f'{self.id}.{self.file.name.split(".")[-1]}'  noqa: E800
        self.audio_file.name = f'{self.id}'
        super().save(*args, **kwargs)

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."compositions"'
        verbose_name = _('composition')
        verbose_name_plural = _('compositions')

    def __str__(self):
        return f'{self.title} ({self.genre})'


class MusicianComposition(models.Model):
    musician = models.ForeignKey(
        Musician,
        verbose_name=_('musician'),
        on_delete=models.CASCADE,
    )
    composition = models.ForeignKey(
        Composition,
        verbose_name=_('composition'),
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = f'"{SCHEMA_NAME}"."musicians_compositions"'
        unique_together = ('musician', 'composition')
        verbose_name = _('relationship musician-composition')
        verbose_name_plural = _('relationships musician-composition')

    def __str__(self):
        return f'{self.musician} - {self.composition}'
