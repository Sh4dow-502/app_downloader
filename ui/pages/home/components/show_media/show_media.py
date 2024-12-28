import flet as ft

from .media_info.media_info import MediaInfo
from ..media_select import MediaSelect
from ...widgets import DownloadButton
from domain.functions.download import DownloadMedia
from domain.models import DownloadState
from domain.states import SearchState


class ShowMedia(ft.Container):
    def __init__(self):
        super().__init__()
        self.media_downloaded = []
        self.margin = ft.margin.only(top=15)

        self.media_info = MediaInfo()
        self.media_select = MediaSelect(function_switch=self.switch_function)
        self.download_button = DownloadButton(
            text="Descargar", function=self.download_media
        )

        self.content = ft.Column(
            controls=[
                self.media_info,
                self.media_select,
                self.download_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def download_media(self):
        self.download_button.text_widget.value = "Descargando"
        self.download_button.function = None
        self.media_select.disable = True
        self.update()

        DownloadState.state = "downloading"

        download = DownloadMedia(
            url=self.media_info.url_video,
            hook_function=self.download_hook,
            post_processor=self.download_convert,
        )

        if self.media_select.is_selected == "music":
            self.media_downloaded.append("music")
            download.download_music()
        elif self.media_select.is_selected == "video":
            self.media_downloaded.append("video")
            download.download_video()

    def downloading(self, percent):
        try:
            calc_width = 200 / 100 * float(percent)
            if calc_width <= 200:
                self.download_button.progress_gradient.width = calc_width
        except Exception as _:
            pass
        self.update()

    def download_end(self):
        self.download_button.text_widget.value = "Convirtiendo"
        self.update()

    def download_convert(self):
        self.download_button.text_widget.value = "Completado"
        self.media_select.disable = False
        DownloadState.state = "completed"
        SearchState.state = "on"
        self.update()

    def download_hook(self, d):
        if d["status"] == "downloading":
            percent = d["_percent_str"]
            try:
                percent = float(percent.replace("%", ""))
                self.downloading(percent)
            except Exception as e:
                print(e)
        elif d["status"] == "finished":
            self.download_end()

    def switch_function(self, media_switch):
        if media_switch in self.media_downloaded:
            self.download_button.text_widget.value = "Completado"
            self.download_button.progress_gradient.width = 200
            self.download_button.function = None
            self.update()

        else:
            self.download_button.text_widget.value = "Descargar"
            self.download_button.progress_gradient.width = 0
            self.download_button.function = self.download_media
            self.update()
