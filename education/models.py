from django.db import models

# Create your models here.
class Education(models.Model):
    school = models.CharField(max_length=100, null=True)
    education_type = models.CharField(max_length=100, null=True)
    field_of_study = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=500, null=True)


    def __str__(self):
        return f"{self.school} - {self.field_of_study}"