from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="board"),
    path("questions/<int:question_id>/", views.question, name="question")
]