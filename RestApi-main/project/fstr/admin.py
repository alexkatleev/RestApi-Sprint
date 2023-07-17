from django.contrib import admin
from .models import *


class PerevalAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'beauty_title',
                    'title',
                    'other_titles',
                    'add_time',
                    'status',
                    'connect',)


class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'latitude',
                    'longitude',
                    'height', )


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'add_time', )


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'winter',
                    'summer',
                    'autumn',
                    'spring', )


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'fam',
                    'name',
                    'otc',
                    'phone', )


admin.site.register(Users, UsersAdmin)
admin.site.register(Pereval, PerevalAdmin)
admin.site.register(Coordinates, CoordinatesAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Level, LevelAdmin)
