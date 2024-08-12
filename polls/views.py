from django.http import HttpResponse

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Question
from django.views import View
from django.shortcuts import redirect, reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Choice


class IndexView(ListView):
    model = Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pub_date')[:5]


class DetailsView(DetailView):
    model = Question


def owner(request):
    return HttpResponse("Hello, world. 74398c40 is the polls owner.")


class ManuallyProtectedView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            loginUrl = reverse("login")+"?"+urlencode({"next": request.path})
            return redirect(loginUrl)
        return HttpResponse("manually protected data")


class ProtectedView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("protected data")


def vote(request, pk):
    choice_id = request.POST.get("choice")
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    return redirect(to=reverse("result", args=(pk,)))


class ResultView(DetailView):
    model = Question
    template_name = "polls/question_result.html"
