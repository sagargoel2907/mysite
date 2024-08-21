from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Make(models.Model):
    name = models.CharField(max_length=128, validators=[MinLengthValidator(
        limit_value=2, message="Name must be greater than 1 character")],
        help_text="Enter the name (e.g. Dodge)")

    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(max_length=128, validators=[MinLengthValidator(
        limit_value=2, message="Nickname must be greater than 1 character")])
    make = models.ForeignKey(to=Make, on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.nickname
