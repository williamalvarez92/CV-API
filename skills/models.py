from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Skills (models.Model):
  name = models.CharField(max_length=50, null=True)

  def __str__(self):
        return f"{self.name}"