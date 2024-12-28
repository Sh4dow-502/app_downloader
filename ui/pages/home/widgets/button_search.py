import flet as ft


class ButtonSearch(ft.Container):
    def __init__(self, search_func=None):
        super().__init__()
        self.search_func = search_func

        self.bgcolor = "#1b1b27"
        self.border_radius = ft.border_radius.all(12)

        self.content = ft.Icon(
            ft.Icons.SEARCH,
            color="#13131b",
        )

        self.padding = ft.padding.all(9)

        self.on_click = self.search

    def search(self, _):
        if self.search_func:
            self.search_func()
