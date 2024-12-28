from yt_dlp import YoutubeDL, postprocessor


class CustomPostProcessor(postprocessor.PostProcessor):
    def __init__(self, function=None):
        super().__init__()
        self.function = function

    def run(self, information):
        self.to_screen("Descarga terminada")
        print(self._progress_hooks)
        if self.function:
            self.function()
        return [], information


class DownloadMedia:
    def __init__(self, url: str, hook_function, post_processor=None):
        self.url = url
        self.hook_function = hook_function
        self.post_processor = post_processor

    def custom_processor(self, _):
        print(_)

    def download_video(self):
        video_options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "~/Descargas/YTDownloader/video/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "noplaylist": False,
            "progress_hooks": [self.hook_function],
            "quiet": True,  # Silencia la salida estándar
            "no_warnings": True,  # Evita mostrar advertencias
            "postprocessors": [
                {"key": "EmbedThumbnail"},
            ],
            "writethumbnail": True,  # Descarga el thumbnail como un archivo separado
            "embedthumbnail": True,
        }

        with YoutubeDL(video_options) as ydl:
            ydl.add_post_processor(CustomPostProcessor(self.post_processor))
            ydl.download([self.url])

    def download_music(self):
        FFMPEG_PATH = "/home/santos/workspace/python/downloader_app_rev/ffmpeg.so"
        music_options = {
            "format": "bestaudio/best",
            "outtmpl": "~/Descargas/YTDownloader/music/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                },
                {"key": "EmbedThumbnail"},
            ],
            "noplaylist": False,
            "progress_hooks": [self.hook_function],
            "quiet": True,  # Silencia la salida estándar
            "no_warnings": True,  # Evita mostrar advertencias
            "writethumbnail": True,  # Descarga el thumbnail como un archivo separado
            "embedthumbnail": True,
        }

        with YoutubeDL(music_options) as ydl:
            ydl.add_post_processor(CustomPostProcessor(self.post_processor))
            ydl.download([self.url])
