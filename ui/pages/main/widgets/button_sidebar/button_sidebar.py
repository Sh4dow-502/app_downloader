import flet as ft


class ButtonSideBar(ft.Container):
    def __init__(
        self,
        master: ft.Page,
        icon: str | None = None,
        function=None,
        bgcolor: str | None = None,
        icon_color: str | None = "#4a4a5a",
        icon_size: ft.OptionalNumber | None = None,
    ):
        super().__init__()

        self.master = master
        self.function = function
        self.bgcolor = bgcolor
        self.icon_color = icon_color
        self.icon = icon
        self.alignment = ft.alignment.center
        self.icon_size = icon_size

        self.width = 40
        self.height = 40

        self.border_radius = ft.border_radius.all(10)

        self.content = ft.Icon(self.icon, color=self.icon_color, size=self.icon_size)

        self.on_click = self.press_button

    def press_button(self, _):
        if self.function:
            self.function()
