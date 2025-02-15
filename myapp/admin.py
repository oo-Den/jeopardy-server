from django.contrib import admin
from .models import Board, Column, Card

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'get_columns', 'get_cards_num']

    @admin.display(description="Columns")
    def get_columns(self, obj: Board):
        return ", ".join([str(col) for col in obj.columns.all()])

    @admin.display(description="Cards")
    def get_cards_num(self, obj: Board):
        return sum([col.cards.count() for col in obj.columns.all()])

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title', 'get_cards']

    @admin.display(description="Cards")
    def get_cards(self, obj: Column):
        return "; ".join([str(card) for card in obj.cards.all()])

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    fields = ['front', 'back']
