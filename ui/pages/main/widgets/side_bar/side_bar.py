import flet as ft

from ..button_sidebar import ButtonSideBar


class SideBar(ft.Container):
    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master

        self.width = 70
        self.border_radius = ft.border_radius.all(13)

        self.bgcolor = ft.Colors.PRIMARY_CONTAINER

        self.content = ft.Column(
            controls=[
                TopButtons(self.master),
                BottomButtons(self.master),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


class BottomButtons(ft.Container):
    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master
        self.margin = ft.margin.only(bottom=17)

        self.content = ButtonSideBar(
            self.master,
            icon=ft.Icons.SETTINGS_ROUNDED,
            icon_color=ft.Colors.GREY_400,
            icon_size=20,
        )


class TopButtons(ft.Column):
    def __init__(self, master: ft.Page):
        super().__init__()

        self.master = master

        self.home_button = ButtonSideBar(
            self.master,
            icon=ft.Icons.HOME_ROUNDED,
            icon_color=ft.Colors.WHITE,
            bgcolor="#1e1e29",
            icon_size=20,
        )

        self.history_button = ButtonSideBar(
            self.master,
            icon=ft.Icons.HISTORY_ROUNDED,
            icon_size=20,
        )

        self.musics_button = ButtonSideBar(
            self.master,
            icon=ft.Icons.MUSIC_NOTE_ROUNDED,
            icon_size=20,
        )

        self.videos_button = ButtonSideBar(
            self.master,
            icon=ft.Icons.VIDEO_FILE_ROUNDED,
            icon_size=20,
        )

        self.controls = [
            ft.Container(),
            self.home_button,
            self.history_button,
            self.musics_button,
            self.videos_button,
        ]

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.spacing = 18
