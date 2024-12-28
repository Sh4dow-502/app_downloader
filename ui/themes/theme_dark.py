import flet as ft


class ThemeDark(ft.Theme):
    def __init__(self):
        super().__init__()

        self.color_scheme = ft.ColorScheme(
            background="#13131b",
        )
        self.scaffold_bgcolor = "#13131b"
