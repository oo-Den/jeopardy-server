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
            "flexible_layout": False,
            "columns": [
                {
                    "title": f"title {i}",
                    "cards": [
                        {
                            "id": randint(1, 65535),
                            "value": j
                        } for j in range(value, value * rows + 1, value)
                    ]
                } for i in range(6)
            ]
        }
    })

def question(request: HttpRequest, question_id: int):
    return render(request, "myapp/question-screen.html", {
        "players": [
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
            {'name': 'irata'},
        ],
        "question": {"id": question_id, "text": "Lorem ipsum"}
    })