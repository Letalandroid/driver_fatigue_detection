from flet import *
from gui.resources.resources_path import (ImagePaths, FontsPath)


class Start:
    def __init__(self, page):
        super().__init__()
        self.images = ImagePaths()
        self.fonts = FontsPath()

        self.page = page

        self.page.fonts = {
            "Brittany": self.fonts.brittany_font,
            "Cardo": self.fonts.cardo_font
        }

    def main(self):
        iniciar_button = ElevatedButton(
            text="Iniciar",
            on_click=self.start,
            bgcolor='#2a2a2a',
            color='#FFFFFF',
            width=180,
            height=40,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),
            )
        )

        center_column = Column(
            controls=[
                Container(height=30),
                Container(height=100),
                iniciar_button,
                Container(height=80),
            ],
            alignment='center',
            horizontal_alignment='center',
            spacing=20,
            expand=True
        )

        elements = Container(
            content=Row(
                controls=[
                    center_column
                ],
                alignment='spaceEvenly',
                vertical_alignment='center',
            ),
            bgcolor="#fffffe",
            padding=0,
            expand=True
        )
        return elements

    def start(self, e):
        self.page.go("/drowsiness_page")
