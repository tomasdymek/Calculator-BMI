
from django.db import models

class BMI(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()

    def __str__(self):
        return f"BMI: {self.bmi}"


class BMI_prototype(models.Model):
    calories = models.IntegerField()