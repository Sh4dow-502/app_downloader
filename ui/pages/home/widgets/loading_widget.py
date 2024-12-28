import asyncio
import flet as ft


class LoadingWidget(ft.Container):
    def __init__(self):
        super().__init__()

        self.width = 185
        self.height = 185
        self.margin = ft.margin.only(top=65)
        self.border_radius = ft.border_radius.all(1000)
        self.bgcolor = "#1b1b27"
        self.padding = ft.padding.all(2)

        self.background_gradient = ft.Container(
            content=ft.Text("Helo world"),
        )

        self.background_gradient = ft.Container(
            width=self.width,
            height=self.height,
            alignment=ft.alignment.top_center,
            content=ft.Container(
                width=15,
                height=15,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        "#56ceff",
                        "#5665ff",
                        "#8756ff",
                    ],
                ),
                border_radius=ft.border_radius.all(1000),
            ),
        )

        self.hide_background = ft.Container(
            width=self.width,
            height=self.height,
            bgcolor="#13131b",
            border_radius=ft.border_radius.all(1000),
            margin=ft.margin.all(15),
        )

        self.text_content = ft.Container(
            width=self.width,
            height=self.height,
            alignment=ft.alignment.center,
            content=ft.Text("CARGANDO"),
        )

        self.content = ft.Stack(
            controls=[
                self.background_gradient,
                self.hide_background,
                self.text_content,
            ],
            alignment=ft.alignment.top_center,
        )

    async def rotate_animation(self):
        rotate = 0

        while True:
            rotate -= 0.01
            num_round = round(rotate, 2)

            if num_round == -6.3:
                await asyncio.sleep(0.1)
            elif num_round > -3.7:
                await asyncio.sleep(0.003)
            else:
                await asyncio.sleep(0.001)
            self.background_gradient.rotate = ft.Rotate(angle=rotate)

            if num_round == -6.3:
                rotate = 0
            self.update()

    def did_mount(self):
        self.page.run_task(self.rotate_animation)
