from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Question(models.Model):

    text = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Choice(models.Model):

    text = models.CharField(max_length=25)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Choice")
        verbose_name_plural = ("Choices")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
