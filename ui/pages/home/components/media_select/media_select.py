import flet as ft


class MediaSelect(ft.Container):
    def __init__(self, function_switch=None, disable=False):
        super().__init__()

        self.disable = disable

        self.is_selected = "music"
        self.function_switch = function_switch
        self.margin = ft.margin.only(top=25)

        self.button_music = ft.Container(
            bgcolor="#2b2b3c",
            width=20,
            height=20,
            border_radius=ft.border_radius.all(100),
            padding=(
                ft.padding.all(3)
                if self.is_selected == "music"
                else ft.padding.all(100)
            ),
            content=ft.Container(
                expand=True,
                bgcolor=ft.Colors.BLUE,
                border_radius=ft.border_radius.all(100),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[
                        "#56ceff",
                        "#5665ff",
                        "#8756ff",
                    ],
                ),
            ),
        )

        self.text_music = ft.Text(
            "Music", color=None if self.is_selected == "music" else ft.Colors.GREY
        )

        self.button_video = ft.Container(
            bgcolor="#2b2b3c",
            width=20,
            height=20,
            border_radius=ft.border_radius.all(100),
            padding=(
                ft.padding.all(3)
                if self.is_selected == "video"
                else ft.padding.all(100)
            ),
            content=ft.Container(
                expand=True,
                bgcolor=ft.Colors.BLUE,
                border_radius=ft.border_radius.all(100),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[
                        "#56ceff",
                        "#5665ff",
                        "#8756ff",
                    ],
                ),
            ),
        )

        self.text_video = ft.Text(
            "Video",
            color=None if self.is_selected == "video" else ft.Colors.GREY,
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.button_music,
                            self.text_music,
                        ]
                    ),
                    on_click=self.switch_music,
                ),
                ft.Container(width=25),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.button_video,
                            self.text_video,
                        ],
                    ),
                    on_click=self.switch_video,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def switch_music(self, _):
        if not self.disable:
            self.button_music.padding = ft.padding.all(3)
            self.text_music.color = None

            self.button_video.padding = ft.padding.all(100)
            self.text_video.color = ft.Colors.GREY

            self.is_selected = "music"
            if self.function_switch:
                self.function_switch(self.is_selected)
            self.update()

    def switch_video(self, _):
        if not self.disable:
            self.button_video.padding = ft.padding.all(3)
            self.text_video.color = None

            self.button_music.padding = ft.padding.all(100)
            self.text_music.color = ft.Colors.GREY

            self.is_selected = "video"
            if self.function_switch:
                self.function_switch(self.is_selected)
            self.update()
