from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="board"),
    path("questions/<int:column_id>/<int:card_id>/", views.question, name="question")
]