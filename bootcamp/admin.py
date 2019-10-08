from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class LieuAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
    )
    search_fields = ('name',)


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        )
    search_fields = ('name',)


class EncadreurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'specialite',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'specialite',
        'status',
        'date_add',
        )


class EtudiantAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'contact',
        'specialite',
        'lieu',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'specialite',
        'lieu',
        'status',
        'date_add',
        )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Lieu, LieuAdmin)
_register(models.Specialite, SpecialiteAdmin)
_register(models.Encadreur, EncadreurAdmin)
_register(models.Etudiant, EtudiantAdmin)
