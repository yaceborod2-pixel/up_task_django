from django.urls import path
from .views.Tasks import Tasks

urlpatterns = [
    path("", Tasks.as_view(), name="list")
]
