from django.contrib import admin
from Variedades.models import Variety

#admin.site.register(Variety)

@admin.register(Variety)
class Variety_admin(admin.ModelAdmin):
    list_display = ['name', 'appearance', 'smell', 'taste']
