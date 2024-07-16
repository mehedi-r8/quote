from django.db import models


class Antonym(models.Model):
    word = models.CharField(max_length=100)
    antonym = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word} - {self.antonym}"
