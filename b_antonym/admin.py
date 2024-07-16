from django.contrib import admin
from .models import Antonym

@admin.register(Antonym)
class AntonymAdmin(admin.ModelAdmin):
    list_display = ('word', 'antonym')
    search_fields = ('word', 'antonym')
