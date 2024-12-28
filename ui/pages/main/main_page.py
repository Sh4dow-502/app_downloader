import flet as ft


class MainPage(ft.View):
    def __init__(self, master: ft.Page):
        super().__init__()

        self.master = master
        self.expand = True
        self.padding = ft.padding.all(0)

        self.controls = [
            ft.Container(
                padding=ft.padding.all(12),
                alignment=ft.alignment.center,
                content=ft.Row(
                    controls=[
                        SideBar(master=self.master),
                        MainContainer(master=self.master),
                    ],
                    spacing=20,
                ),
            )
        ]


class SideBar(ft.Container):
    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master

        self.width = 70
        self.height = 660
        self.border_radius = ft.border_radius.all(13)

        self.bgcolor = ft.Colors.PRIMARY_CONTAINER


class MainContainer(ft.Container):
    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master

        self.expand = True
        self.width = self.master.width - 70
        self.height = 660
        self.border_radius = ft.border_radius.all(13)

        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
