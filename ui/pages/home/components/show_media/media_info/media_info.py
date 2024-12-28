import flet as ft

from .media_image import MediaImage
from domain.models import MediaModel


class MediaInfo(ft.Container):
    def __init__(self):
        super().__init__()

        # self.data_dict = {
        #     "author": "R4A1",
        #     "duration": "0:3:07",
        #     "title": "R4A1 - ANOTHER",
        #     "thumbnail": "https://i.ytimg.com/vi/_yCUbhOz0u4/maxresdefault.jpg",
        #     "url": "https://youtu.be/_yCUbhOz0u4?si=31M7WchMOhhlHSVl",
        # }
        # self.other = MediaModel.from_dict(self.data_dict)
        # self.data_test = MediaModel.to_map()
        self.data = MediaModel
        self.url_video = self.data.url

        self.content = ft.Column(
            controls=[
                ft.Text(
                    self.data.author,
                    max_lines=2,
                    size=15,
                ),
                ft.Text(
                    f"{self.data.duration}",
                    size=14,
                    color=ft.Colors.GREY_600,
                ),
                MediaImage(url_image=self.data.thumbnail, url_video=self.data.url),
                ft.Container(),
                ft.Text(
                    self.data.title,
                    max_lines=2,
                    width=500,
                    size=16,
                    text_align=ft.TextAlign.CENTER,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
