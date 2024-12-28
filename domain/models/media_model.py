class MediaModel:
    id = 0
    title: str = ""
    author: str = ""
    duration: float = 0.0
    thumbnail: str = ""
    url: str = ""

    @classmethod
    def from_dict(cls, data):
        cls.title = data["title"]
        cls.author = data["author"]
        cls.duration = data["duration"]
        cls.thumbnail = data["thumbnail"]
        cls.url = data["url"]

    @classmethod
    def to_map(cls):
        return {
            "title": cls.title,
            "author": cls.author,
            "duration": cls.duration,
            "thumbnail": cls.thumbnail,
            "url": cls.url,
        }

    # def __str__(self) -> str:
    #     return (
    #         f"id: {self.id}\n"
    #         f"title: {self.title}\n"
    #         f"author: {self.author}\n"
    #         f"duration: {self.duration}\n"
    #         f"thumbnail: {self.thumbnail}\n"
    #         f"url: {self.url}"
    #     )
