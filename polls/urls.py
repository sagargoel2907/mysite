from django.urls import path
from . import views

urlpatterns = [path("", views.IndexView.as_view(), name="polls"),
               path("owner", views.owner, name="owner")]
