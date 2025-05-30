from django.urls import path

from . import views

urlpatterns = [
    path("boards/<int:board_id>/", views.board, name="board"),
    path("boards/<int:board_id>/questions/<int:column_id>/<int:card_id>/", views.question, name="question")
]
