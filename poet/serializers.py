from rest_framework import serializers
from .models import Poet, Book, FamousBook, Text, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    #publication_year = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'category',]

    def get_publication_year(self, obj):
        return FamousBook.objects.filter(poet=obj.poet, title=obj.title).first().publication_year

class FamousBookSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = FamousBook
        fields = ['title', 'category', 'publication_year']

class TextSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Text
        fields = ['category', 'content']

class PoetSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    famous_books = FamousBookSerializer(many=True, read_only=True)
    texts = TextSerializer(many=True, read_only=True)

    class Meta:
        model = Poet
        fields = ['name', 'birth_year', 'death_year', 'birth_place', 'picture', 'books', 'texts', 'famous_books']
