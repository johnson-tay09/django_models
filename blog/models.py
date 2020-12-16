from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.author}'
