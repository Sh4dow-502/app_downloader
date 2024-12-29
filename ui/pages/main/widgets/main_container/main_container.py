import flet as ft


class MainContainer(ft.Container):
    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master

        self.expand = True
        self.border_radius = ft.border_radius.all(13)

        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
