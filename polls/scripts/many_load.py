from polls.models import Question, Choice
import csv
from django.utils import timezone


def run():
    Question.objects.all().delete()
    Choice.objects.all().delete()

    fhandler = open("polls/polls_data.csv")
    reader = csv.reader(fhandler)
    next(reader)
    now = timezone.now()
    for row in reader:
        q, *choices = row
        q = Question(question_text=q, pub_date=now)
        q.save()
        for c in choices:
            Choice(choice_text=c, question=q).save()
