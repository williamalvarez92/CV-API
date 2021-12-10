from django.db import models

# Create your models here.
class Social (models.Model):
  linkedIn = models.URLField(max_length=150, null=True)
  gitHub = models.URLField(max_length= 150, null=True)
  codeWars = models.URLField(max_length= 150, null=True)
  codePen = models.URLField(max_length=150, null=True)
  website = models.URLField(max_length=150, null=True)
