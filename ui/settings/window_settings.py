import flet as ft


def window_settings(page: ft.Page):

    # En linux no funciona si window.title_bar_hidden esta activo
    page.window.width = 900
    page.window.height = 680
    page.fonts = {
        "Super Sense": "/fonts/SuperSense.ttf",
        "Loving Snow": "/fonts/LovingSnow.otf",
        "Weekend Camp": "/fonts/WeekendCamp.otf",
        "Funny Face": "/fonts/FunnyFace.otf",
        "Love Dear": "/fonts/LoveDear.otf",
    }

    # En linux no funciona
    # page.window.title_bar_hidden = True

    # En linux no funciona
    # page.window.resizable = False
