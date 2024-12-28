import flet as ft


class Title(ft.Text):
    def __init__(self):
        super().__init__()

        self.spans = [
            ft.TextSpan(
                "YTDOWNLOADER",
                ft.TextStyle(
                    font_family="Super Sense",
                    size=35,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 11),
                            (0, 45),
                            colors=[
                                "#4481ff",
                                "#8156ff",
                            ],
                        ),
                    ),
                    letter_spacing=1,
                ),
            )
        ]
