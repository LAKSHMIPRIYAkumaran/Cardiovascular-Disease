from django.db import models


# Create your models here.


class Cardiovascular_table(models.Model):
    age = models.FloatField(null=True, blank=True, default=25.0)
    cp = models.FloatField(null=True, blank=True, max_length=20)
    trestbps = models.FloatField(null=True, blank=True, max_length=200)
    sex = models.CharField(null=True, blank=True, max_length=10)
    fbs = models.FloatField(null=True, blank=True, default=100)
    restecg = models.FloatField(null=True, blank=True, max_length=30)
    thalach = models.FloatField(null=True, blank=True, max_length=25.0)
    exang = models.FloatField(null=True, blank=True, max_length=100)
    oldpeak = models.FloatField(null=True, blank=True, max_length=100)
    slope = models.CharField(null=True, blank=True, max_length=40)
    ca = models.FloatField(null=True, blank=True, max_length=100)
    thal = models.FloatField(null=True, blank=True, max_length=10) 

    def __str__(self):
        return self.name