from django.db import models

# Create your models here.
class Patient(models.Model):

    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    mrn = models.IntegerField()
    sex = models.CharField(max_length = 5)
    race = models.CharField(max_length=20)
    diagnosis = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name