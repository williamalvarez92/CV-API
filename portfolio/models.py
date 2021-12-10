from django.db import models
# Create your models here.
class Portfolio (models.Model):
    title = models.CharField(max_length=100, null=True)
    repo_link = models.URLField(max_length=500, null=True)
    live_link = models.URLField(max_length=500, null=True)
    description = models.CharField(max_length=800, null=True)
    image = models.ImageField(null=True, upload_to='images/')