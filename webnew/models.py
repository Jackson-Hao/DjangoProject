from django.db import models

class MyModel(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    temperature = models.FloatField()

    @property
    def get_gender_display(self):
        return dict(self.GENDER_CHOICES).get(self.gender)