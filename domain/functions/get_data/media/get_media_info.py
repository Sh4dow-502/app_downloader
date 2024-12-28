import datetime

from yt_dlp import YoutubeDL


class GetMediaInfo:
    def __init__(self, url: str):
        self.url = url

        self.yt_option = {
            "quiet": True,  # Minimizar salida
            "skip_download": True,  # No descargar contenido
            "no_warnings": True,  # No mostrar advertencias
            "extractor_args": {
                "youtube": {
                    "skip": [
                        "comments",  # Evitar datos adicionales como comentarios
                    ]
                }
            },
        }
        self.yt = YoutubeDL(self.yt_option)
        self.info = self.yt.extract_info(self.url, download=False)

    def get(self):

        info = self.yt.extract_info(self.url, download=False)
        if info:
            duration = self.info.get("duration")

            duration = datetime.timedelta(seconds=duration)
            datos = {
                "title": self.info.get("title"),
                "author": self.info.get("uploader"),
                "duration": str(duration),
                "thumbnail": self.info.get("thumbnail"),
            }

            return datos
