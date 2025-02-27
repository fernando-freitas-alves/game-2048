from django.contrib import admin
from django.utils.html import format_html

from .models import GameState


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "user",
        "formatted_board",
        "score",
        "over",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    list_filter = (
        "over",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "uuid",
        "user__username",
        "user__email",
        "created_at",
        "updated_at",
    )
    fields = (
        "uuid",
        "user",
        "formatted_board",
        "score",
        "over",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "uuid",
        "user",
        "formatted_board",
        "score",
        "over",
        "created_at",
        "updated_at",
    )

    def formatted_board(self, obj):
        def get_cell_colors(cell):
            if cell == 0:
                return "#cdc1b4", "#776e65"
            elif cell == 2:
                return "#eee4da", "#776e65"
            elif cell == 4:
                return "#ede0c8", "#776e65"
            elif cell == 8:
                return "#f2b179", "#f9f6f2"
            elif cell == 16:
                return "#f59563", "#f9f6f2"
            elif cell == 32:
                return "#f67c5f", "#f9f6f2"
            elif cell == 64:
                return "#f65e3b", "#f9f6f2"
            elif cell == 128:
                return "#edcf72", "#f9f6f2"
            elif cell == 256:
                return "#edcc61", "#f9f6f2"
            elif cell == 512:
                return "#edc850", "#f9f6f2"
            elif cell == 1024:
                return "#edc53f", "#f9f6f2"
            elif cell == 2048:
                return "#edc22e", "#f9f6f2"
            else:
                return "#cdc1b4", "#776e65"

        board_html = (
            "<table style='border-collapse: collapse; border-spacing: 10px; "
            "background-color: #bbada0; border-radius: 5px;'>"
        )
        cell_size = "30px"
        for row in obj.board:
            board_html += "<tr style='padding: 10px;'>"
            for cell in row:
                bg_color, text_color = get_cell_colors(cell)
                display_value = cell if cell != 0 else ""
                board_html += (
                    "<td style='border: 4px solid #bbada0; border-radius: 10px; padding: 5px; font-weight: bold;"
                    f"width: {cell_size}; min-width: {cell_size}; max-width: {cell_size}; "
                    f"height: {cell_size}; min-height: {cell_size}; max-height: {cell_size}; "
                    f"background-color: {bg_color}; color: {text_color}; text-align: center; vertical-align: middle;"
                    f"'>{display_value}</td>"
                )
            board_html += "</tr>"
        board_html += "</table>"
        return format_html(board_html)

    formatted_board.short_description = "Board"  # type: ignore[attr-defined]
