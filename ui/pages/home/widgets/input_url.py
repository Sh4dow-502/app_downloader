import flet as ft


class InputUrl(ft.Container):
    def __init__(self, on_focus=None, on_blur=None, on_change=None):
        super().__init__()
        self.on_focus = on_focus
        self.on_blur = on_blur
        self.on_change = on_change

        self.value = ""

        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(12)
        self.width = 452
        self.height = 48

        self.gradient_background = ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[
                "#56f5ff",
                "#566aff",
                "#6a56ff",
                "#8756ff",
            ],
        )

        self.text_field = ft.TextField(
            hint_text="Link",
            hint_style=ft.TextStyle(
                color=ft.Colors.GREY_700,
            ),
            text_align=ft.TextAlign.LEFT,
            text_vertical_align=ft.VerticalAlignment.CENTER,
            bgcolor="#1b1b27",
            width=450,
            height=46,
            border_radius=ft.border_radius.all(12),
            border_width=0,
            on_focus=self.input_focus,
            on_blur=self.input_blur,
            on_change=self.input_change,
        )
        self.content = self.text_field

    def input_focus(self, _):
        self.gradient = self.gradient_background
        self.update()

        if self.on_focus:
            self.on_focus()

    def input_blur(self, _):
        if not self.text_field.value:
            self.gradient = None
            self.update()

        if self.on_blur:
            self.on_blur()

    def input_change(self, _):
        self.value = self.text_field.value
        if self.on_change:
            self.on_change(self.text_field.value)
