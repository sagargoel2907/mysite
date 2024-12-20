from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=200, validators=[
        MinLengthValidator(2, "Must be atleast 2 character")])

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=200, validators=[
        MinLengthValidator(2, "Must be atleast 2 characters")])
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=200)
    breed = models.ForeignKey(to=Breed, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
