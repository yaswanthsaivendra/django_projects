from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}'