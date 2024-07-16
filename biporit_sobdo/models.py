from django.db import models


class OppositeWord(models.Model):
    word = models.CharField(max_length=255)
    opposite = models.CharField(max_length=255)

    class Meta:
        ordering = ['word']  # Ascending order by word

    def __str__(self):
        return f"{self.word} = {self.opposite}"
