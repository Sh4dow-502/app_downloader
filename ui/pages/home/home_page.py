from threading import Thread

import flet as ft

from .components import SearchMedia
from .components import ShowMedia
from .widgets import Title
from .widgets import LoadingWidget
from domain.models import MediaModel
from domain.models import DownloadState
from domain.states import SearchState

from domain.functions.get_data import GetMediaInfo


class HomePage(ft.View):

    def __init__(self, master: ft.Page):
        super().__init__()
        self.master = master
        self.route = "/"
        self.bgcolor = "#13131b"

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.loading_widget = LoadingWidget()

        self.controls = [
            Title(),
            SearchMedia(function_search=self.search_media),
        ]

    def remove_widget(self, widget):

        if widget in self.controls:
            self.controls.remove(widget)
            self.update()

    def add_widget(self, widget):
        self.controls.append(widget)
        self.update()

    def get_media_data(self, url):
        get_media = GetMediaInfo(url=url)
        media_info = get_media.get()
        media_info["url"] = url

        MediaModel.from_dict(media_info)

        self.remove_widget(self.loading_widget)

        DownloadState.state = "completed"
        SearchState.state = "on"

        self.add_widget(ShowMedia())

    def search_media(self, url: str):
        try:
            del self.controls[2]
        except Exception as _:
            pass
        self.add_widget(self.loading_widget)
        tr = Thread(target=self.get_media_data, args=(url,))
        tr.start()
