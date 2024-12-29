import flet as ft

from .widgets import SideBar
from .widgets import MainContainer


class MainPage(ft.View):
    def __init__(self, master: ft.Page):
        super().__init__()

        self.master = master
        self.padding = ft.padding.all(0)

        self.controls = [
            ft.Container(
                padding=ft.padding.all(15),
                alignment=ft.alignment.center,
                content=ft.Row(
                    controls=[
                        SideBar(master=self.master),
                        MainContainer(master=self.master),
                    ],
                    spacing=20,
                ),
                expand=True,
            )
        ]
