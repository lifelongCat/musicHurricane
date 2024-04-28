from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Award, Composition, Musician, MusicianComposition


class AwardInline(admin.TabularInline):
    model = Award
    verbose_name = _('relationship musician-award')
    verbose_name_plural = _('relationships musician-award')
    extra = 1


class MusicianCompositionInline(admin.TabularInline):
    model = MusicianComposition
    verbose_name = _('relationship musician-composition')
    verbose_name_plural = _('relationships musician-composition')
    extra = 1


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    # add "save as new" button
    save_as = True

    # add and change pages
    fields = ('id', 'title', 'musician', 'year')
    readonly_fields = ('id',)

    # view page
    list_display = ('title', 'musician', 'year')
    list_display_links = ('title',)

    ordering = ('title', 'musician')
    sortable_by = ('title', 'year', 'musician')

    list_filter = ('title', 'musician__first_name', 'musician__last_name', 'year')
    search_fields = ('title', 'musician__first_name', 'musician__last_name')
    search_help_text = _('search by title or musician')


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    # add "save as new" button
    save_as = True

    # add and change pages
    fields = ('id', 'title', 'genre', 'duration')
    readonly_fields = ('id',)

    # view page
    list_display = ('title', 'genre', 'duration')
    list_display_links = ('title',)

    ordering = ('title', 'genre', '-duration')
    sortable_by = ('title', 'genre', 'duration')

    list_filter = ('title', 'genre', 'duration')
    search_fields = ('title',)
    search_help_text = _('search by title')

    # many to many inline (add and change page)
    inlines = (MusicianCompositionInline,)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    # add "save as new" button
    save_as = True

    # add and change pages
    fields = ('id', 'first_name', 'last_name', 'birth_date')
    readonly_fields = ('id',)

    # view page
    list_display = ('first_name', 'last_name', 'birth_date')
    list_display_links = ('first_name', 'last_name')

    ordering = ('first_name', 'last_name', 'birth_date')
    sortable_by = ('first_name', 'last_name', 'birth_date')

    list_filter = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')
    search_help_text = _('search by first or last name')

    # one to many and many to many inlines (add and change page)
    inlines = (AwardInline, MusicianCompositionInline)


@admin.register(MusicianComposition)
class MusicianCompositionAdmin(admin.ModelAdmin):
    # add "save as new" button
    save_as = True

    # add and change pages
    fields = ('musician', 'composition')

    # view page
    list_display = ('musician', 'composition')
    list_display_links = ('musician', 'composition')

    ordering = ('musician', 'composition')
    sortable_by = ('musician', 'composition')

    list_filter = (
        'musician__first_name', 'musician__last_name', 'composition__title', 'composition__genre',
    )
    search_fields = ('musician__first_name', 'musician__last_name', 'composition__title')
    search_help_text = _('search by musician first name, musician last name or composition title')
