import flet as ft


class MediaImage(ft.Container):
    def __init__(self, url_image: str, url_video):
        super().__init__()

        self.url = url_video

        self.col = 6

        self.width = 200
        self.height = 165

        self.border_radius = ft.border_radius.all(18)
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(0)

        self.content = ft.Image(
            src=url_image,
            width=200,
            height=165,
            expand=True,
            fit=ft.ImageFit.COVER,
        )
