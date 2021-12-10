from django.db import models


# Create your models here.
class Work(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    role_tile = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=1000, null=True)
    company_url = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return f"{self.company_name} - {self.role_tile}"