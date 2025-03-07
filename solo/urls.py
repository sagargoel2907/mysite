from django.urls import path
from .views import MyView

app_name = 'solo'
urlpatterns = [
    path('', MyView.as_view(), name='solo'),
]
