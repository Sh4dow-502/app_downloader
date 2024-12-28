import flet as ft
from ui import pages
from ui import settings


async def main(page: ft.Page):
    settings.window_settings(page)

    def route_change(_):
        page.views.clear()

        if page.route == "/":
            page.views.append(pages.HomePage(page))

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
