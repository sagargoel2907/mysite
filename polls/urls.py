from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="polls"),
               path("owner", views.owner, name="owner")]
