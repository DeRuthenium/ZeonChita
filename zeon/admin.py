from django.contrib import admin

from zeon.models import *

@admin.register(Computers)
class ComputersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cpu',
        'gpu',
        'operativka',
        'mother',
        'ssd',
        'hdd',
        'corpus',
        'perifiria',
        'photo_tag',
    ]

    list_filter = [
        'operativka',
        'ssd',
        'hdd',
    ]
    save_as = True
    save_on_top = True

@admin.register(Tarifs)
class TarifsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'opisanie',
        'price',
        'photo_tag',
    ]

    list_filter = [
        'price',

    ]
    save_as = True
    save_on_top = True
