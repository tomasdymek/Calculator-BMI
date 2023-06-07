from django.db import models
from datetime import datetime


# Create your models here.


BMI_STATUS_GENDER = (
    ('men', 'Men'),
    ('woman', 'Woman')
)


class Bmi(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    result = models.FloatField(null=True, blank=True)
    bmi = models.FloatField()
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(choices=BMI_STATUS_GENDER, max_length=35, default=True)

    def __str__(self):
        return self.user.username


PHYSICAL_ACTIVITY_LEVEL = (
    ('no', 'No physical activity'),
    ('little', 'Little physical activity (1-3 times a week)'),
    ('average', 'Average physical activity (3-5 times a week)'),
    ('high', 'High physical activity (daily physical activity)')
)


class Calories(models.Model):
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    status = models.CharField(choices=PHYSICAL_ACTIVITY_LEVEL, max_length=60, default=True)



