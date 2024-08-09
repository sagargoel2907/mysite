from django.http import HttpResponse

# Create your views here.
from django.views.generic.list import ListView
from .models import Question


class IndexView(ListView):
    model = Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pub_date')[:5]


def owner(request):
    return HttpResponse("Hello, world. 74398c40 is the polls owner.")
