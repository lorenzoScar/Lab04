import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        self._dropLingua = ft.Dropdown(
            label="Seleziona lingua",
            hint_text="Scegli una lingua",
            options=[
                ft.dropdown.Option("englsih"),
                ft.dropdown.Option("italian"),
                ft.dropdown.Option("spanish"),
            ]
        )
        self._row1 = ft.Row(controls=[self._dropLingua])

        self._dropMetodo = ft.Dropdown(
            label="Scegli metodo",
            hint_text="Scegli un metodo",
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic")
            ]
        )

        self._txtInInput = ft.TextField(label="Inserisci testo")

        self._btnSpellCheck = ft.ElevatedButton(text = "Spell Check",
                                           on_click=self.__controller.handleSpellCheck)

        self._row2 = ft.Row(controls=[self._dropMetodo, self._txtInInput, self._btnSpellCheck])

        self._txtOut = ft.ListView(expand=1, spacing=10)
        self.page.add(self._row1, self._row2, self._txtOut)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
