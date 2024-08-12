from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="polls"),
    path("owner", views.owner, name="owner"),
    path("manually-protected", views.ManuallyProtectedView.as_view(),
         name='man-protected'),
    path("protected", views.ProtectedView.as_view(), name='protected'),
    path("<int:pk>/", views.DetailsView.as_view(), name="detail")
]
