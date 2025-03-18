from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
