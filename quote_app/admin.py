from django.contrib import admin
from .models import Writer, Quote

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote', 'writer')
    search_fields = ('quote', 'writer__name')
