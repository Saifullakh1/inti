from django.db import models


class GenderChoice(models.Choices):
    male = 'male'
    female = 'female'


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    age = models.IntegerField(default=0, verbose_name="Возраст")
    gender = models.CharField(max_length=20, choices=GenderChoice.choices, verbose_name="Гендер")

    def __str__(self):
        return self.name
