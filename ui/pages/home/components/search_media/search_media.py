import flet as ft

from ui.pages.home.widgets import InputUrl, ButtonSearch
from domain.states import SearchState


class SearchMedia(ft.Container):
    def __init__(self, function_search=None):
        super().__init__()

        self.function_search = function_search

        self.input_url = InputUrl(on_change=self.on_change_input)
        self.button_search = ButtonSearch(search_func=self.search)

        self.margin = ft.margin.only(top=5)

        self.gradient_bg = ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[
                "#56ceff",
                "#5665ff",
                "#8756ff",
            ],
        )

        self.content = ft.Row(
            controls=[
                self.input_url,
                self.button_search,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    # Detecta que si esta vacio el input, el boton de busqueda no se activa
    def on_change_input(self, text):
        if text:
            self.button_search.gradient = self.gradient_bg
            self.input_url.value = text
            self.button_search.search_func = self.search
        else:
            self.button_search.gradient = None
            self.button_search.search_func = None
        self.update()

    def search(self):
        url = self.input_url.value
        print(self.input_url.value)
        if self.input_url.value and self.function_search:
            print(SearchState.state)
            if SearchState.state == "on":
                SearchState.state = "off"
                self.function_search(url)
                self.input_url.text_field.value = ""
                self.input_url.on_change = self.on_change_input
                self.input_url.gradient = None
                self.input_url.value = ""
                self.button_search.gradient = None
                self.update()
