from django.shortcuts import render
from django.http import HttpRequest
from random import randint

def main(request: HttpRequest):
    rows: int = 5
    value: int = 200
    
    return render(request, "myapp/board-screen.html", {
        "currency_sign": "$",
        "players": [
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
        ],
        "board": {
            "rows": rows,
            "flexible_layout": True,
            "columns": [
                {
                    "title": f"title {i}",
                    "cards": [
                        {
                            "value": j
                        } for j in range(value, value * (i+1) + 1, value)
                    ]
                } for i in range(6)
            ]
        }
    })

def question(request: HttpRequest, column_id: int, card_id: int):
    template_name = "myapp/question-screen.html"

    if "X-Partial" in request.headers:
        template_name += "#" + request.headers["X-Partial"]

    return render(request, template_name, {
        "players": [
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
        ],
        "question": {"text": "Lorem ipsum"}
    })
