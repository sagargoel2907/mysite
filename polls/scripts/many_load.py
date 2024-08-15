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
        q, c1, c2 = row
        q = Question(question_text=q, pub_date=now)
        q.save()
        Choice(choice_text=c1, question=q).save()
        Choice(choice_text=c2, question=q).save()
