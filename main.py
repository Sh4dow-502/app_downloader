import flet as ft
from ui import pages
from ui import settings
from ui.themes import DarkTheme


async def main(page: ft.Page):
    settings.window_settings(page)

    page.dark_theme = DarkTheme()

    def route_change(_):
        page.views.clear()

        if page.route == "/":
            page.views.append(pages.MainPage(page))

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
