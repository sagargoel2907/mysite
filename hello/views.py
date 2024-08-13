from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_view(request):
    num_visits = request.session.get("num_visits", 0)+1
    request.session["num_visits"] = num_visits
    if num_visits > 4:
        del (request.session["num_visits"])

    response_text = f"view count={num_visits}"

    response = HttpResponse(response_text)
    response.set_cookie('dj4e_cookie', '74398c40', max_age=1000)
    return response
