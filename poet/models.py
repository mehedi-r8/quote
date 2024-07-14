from django.db import models


class Poet(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    death_year = models.CharField(max_length=100, default='Alive')
    birth_place = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='poet_pics/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)  # potrika ekhanei hobe
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    poet = models.ForeignKey(Poet, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FamousBook(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='famous_books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    poet = models.ForeignKey(Poet, related_name='famous_books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


class Text(models.Model):
    category = models.ForeignKey(Category, related_name='texts', on_delete=models.CASCADE)
    content = models.TextField()
    poet = models.ForeignKey(Poet, related_name='texts', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]
