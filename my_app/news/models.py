from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')
    owner = models.ForeignKey(User, on_delete=models.SET('Owner was deleted'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
