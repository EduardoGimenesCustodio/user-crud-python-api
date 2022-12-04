from django.db import models

# Create your models here.

class User(models.Model):
    
    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name