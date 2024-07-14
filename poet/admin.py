from django.contrib import admin
from .models import Poet, Category, Book, FamousBook, Text

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class FamousBookInline(admin.TabularInline):
    model = FamousBook
    extra = 1

class TextInline(admin.TabularInline):
    model = Text
    extra = 1

@admin.register(Poet)
class PoetAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'death_year', 'birth_place')
    search_fields = ('name', 'birth_place')
    inlines = [BookInline, FamousBookInline, TextInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'poet')
    search_fields = ('title',)
    list_filter = ('category', 'poet')

@admin.register(FamousBook)
class FamousBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_year', 'poet')
    search_fields = ('title',)
    list_filter = ('category', 'publication_year', 'poet')

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', 'poet')
    search_fields = ('content',)
    list_filter = ('category', 'poet')
