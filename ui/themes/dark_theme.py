import flet as ft


class DarkTheme(ft.Theme):
    def __init__(self):
        super().__init__()

        self.color_scheme = ft.ColorScheme(
            background="#13131b",
            primary_container="#13131b",
            secondary_container="#15151c",
        )
        # self.scaffold_bgcolor = "#15151c"
        self.scaffold_bgcolor = "#1e1e29"
