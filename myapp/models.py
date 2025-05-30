from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    owner = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return f"{self.front} - {self.back}"

class Column(models.Model):
    title = models.CharField(max_length=100)
    cards = models.ManyToManyField(
        Card,
        through="ColumnCell",
        through_fields=("column", "card")
    )
    owner = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Board(models.Model):
    name = models.CharField(max_length=100)
    columns = models.ManyToManyField(
        Column,
        through="BoardColumn",
        through_fields=("board", "column")
    )
    owner = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return self.name

class BoardColumn(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)

    column_number = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['board', 'column_number',], name='unique_board_column')
        ]

    def __str__(self):
        return f"Column {self.column.title} of board {self.board.name}"

class ColumnCell(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    row_number = models.PositiveSmallIntegerField(blank=True, null=True)
    value = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['column', 'row_number',], name='unique_column_card')
        ]
