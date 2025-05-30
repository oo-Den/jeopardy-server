from django.shortcuts import render
from django.http import HttpRequest
from random import randint

from django.db.models import Max

from .models import Board, Column, BoardColumn, ColumnCell, Card


def board(request: HttpRequest, board_id: int):
    board: Board = Board.objects.get(id=board_id)

    data = {
        "currency_sign": "$",
        "players": [
            {"name": "irata"},
            {"name": "irata"},
            {"name": "irata"},
            {"name": "irata"},
        ],
    }

    data["board"] = {
        "num_rows": 0,
        "flexible_layout": False,
    }
    board_column_q = BoardColumn.objects.filter(board=board)

    data["board"]["columns"] = [None] * board_column_q.count()
    for i, board_column in enumerate(board_column_q.all().order_by("column_number")):
        column = {}

        column["title"] = board_column.column.title

        column_cell_q = ColumnCell.objects.filter(column=board_column.column)

        num_rows = column_cell_q.count()
        if num_rows > data["board"]["num_rows"]:
            data["board"]["num_rows"] = num_rows

        column["cards"] = [None] * num_rows
        for j, column_cell in enumerate(column_cell_q.all().order_by("row_number", "value")):
            card = {}

            card["value"] = column_cell.value

            column["cards"][j] = card

        data["board"]["columns"][i] = column

    print(data)

    return render(request, "myapp/board-screen.html", data)


def question(request: HttpRequest, board_id: int, column_id: int, card_id: int):
    template_name = "myapp/question-screen.html"
    if "X-Partial" in request.headers:
        template_name += "#" + request.headers["X-Partial"]

    data = {
        "players": [
            {"name": "irata"},
            {"name": "irata"},
            {"name": "irata"},
            {"name": "irata"},
        ]
    }

    card = (
        ColumnCell.objects.filter(
            column=(
                BoardColumn.objects.filter(board=Board.objects.get(id=board_id))
                .order_by("column_number")[column_id - 1]
                .column
            )
        )
        .order_by("row_number", "value")[card_id - 1]
        .card
    )

    data["question"] = {"text": card.front}

    return render(request, template_name, data)
