from django.contrib import admin
from .models import Board, Column, Card

# Register your models here.

class ColumnInline(admin.TabularInline):
    model = Board.columns.through
    verbose_name = "Column"
    verbose_name_plural = "Columns"
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    fields = ['name', 'owner']
    list_display = ['name', 'get_columns', 'get_cards_num', 'owner', 'id']

    inlines = [ColumnInline]

    @admin.display(description="Columns")
    def get_columns(self, obj: Board):
        return ", ".join([str(col) for col in obj.columns.all()])

    @admin.display(description="Cards")
    def get_cards_num(self, obj: Board):
        return sum([col.cards.count() for col in obj.columns.all()])

class CardInline(admin.TabularInline):
    model = Column.cards.through
    verbose_name = "Card"
    verbose_name_plural = "Cards"
@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    fields = ['title', 'owner']
    list_display = ['title', 'get_cards', 'owner']

    inlines = [CardInline]

    @admin.display(description="Cards")
    def get_cards(self, obj: Column):
        return "; ".join([str(card) for card in obj.cards.all()])

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    fields = ['front', 'back', 'owner']
    list_display = ['get_content', 'owner']

    @admin.display(description="Content")
    def get_content(self, obj: Card):
        return str(obj)
