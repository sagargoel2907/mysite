from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):

    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ("Question")
        verbose_name_plural = ("Questions")

    def __str__(self):
        return self.text


class Choice(models.Model):

    choice_text = models.CharField(max_length=25)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Choice")
        verbose_name_plural = ("Choices")

    def __str__(self):
        return self.text
