from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quote(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return self.quote[:50]
