import flet as ft


class DownloadButton(ft.Container):
    def __init__(self, text: str, function=None, gd_width=0):
        super().__init__()
        self.text = text
        self.function = function
        self.gd_width = gd_width
        self.on_click = self.press_button

        self.width = 200
        self.height = 70
        self.expand = True
        self.padding = ft.padding.all(2)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(15)
        self.margin = ft.margin.only(top=40)

        self.gradient = ft.LinearGradient(
            colors=[
                "#568cff",
                "#6056ff",
                "#7256ff",
            ],
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
        )

        self.progress_gradient = ft.Container(
            width=self.gd_width,
            height=70,
            border_radius=ft.border_radius.all(15),
            gradient=self.gradient,
        )

        self.text_widget = ft.Text(
            self.text,
            size=17,
            weight=ft.FontWeight.W_500,
        )

        self.container_text = ft.Container(
            content=self.text_widget,
            alignment=ft.alignment.center,
        )

        self.content = ft.Stack(
            controls=[
                ft.Container(
                    bgcolor="#13131b",
                    border_radius=ft.border_radius.all(15),
                ),
                self.progress_gradient,
                self.container_text,
            ],
            alignment=ft.alignment.center_left,
        )

    def press_button(self, _):
        if self.function:
            self.function()
