from django.db import models

# Create your models here.
class Table(models.Model):
    field1 = models.CharField('field1', max_length=100)
    field2 = models.CharField('field2', max_length=100)