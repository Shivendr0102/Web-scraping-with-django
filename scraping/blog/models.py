from django.db import models
from django.utils.text import slugify

class Title(models.Model):
    Heading = models.TextField()


    def __str__(self):
        return self.Heading
