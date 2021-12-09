from django.db import models

# Create your models here.
class About(models.Model):
    intro = models.CharField(max_length=1000, null=True)
    interests = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return f"{self.intro} - {self.interests}"