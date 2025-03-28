import reflex as rx
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.styles.colors import Color

def card_portfolio(headers=[], textos=[], enlaces=[], imagenes=[]) -> rx.Component:
    '''Función que devuelve un conjunto de cards distribuidos en dos columnas.'''
    return rx.card(
        rx.grid(
            [
                rx.card(
                    rx.hstack(
                        rx.image(src=imagen, width="50%", height="auto"),
                        rx.divider(orientation="vertical", color="black", size="3", high="100%"),
                        rx.vstack(
                            rx.heading(header, size="6", align="left"),
                            rx.text(texto, align="left", text_align="justify"),
                            rx.link("repositorio en GitHub", href=enlace, is_external=True),
                        ),
                    ),
                    box_shadow="lg",
                    border_radius="10px",
                    padding_y=Size.MEDIUM.value,
                    margin_bottom=Size.VERY_BIG.value,
                    margin_y=Size.MEDIUM.value,
                    margin_x=Size.BIG.value,
                    max_width=MAX_WIDTH,
                    background_color=Color.PRIMARY.value,
                    width="100%"
                )
                for header, texto, enlace, imagen in zip(headers, textos, enlaces, imagenes)
            ],
            columns="2",
            spacing="4",
            width="100%",
        ),
        padding=Size.MEDIUM.value,
        spacing=Size.MEDIUM.value,
        width="100%",
    )

def card_portfolio2(headers= [], textos=[], enlaces=[], imagenes=[]) -> rx.Component:
    '''Función que devuelve un conjunto de botones en un card
    textos: lista de textos de los botones
    enlaces: lista de enlaces a los que llevan los botones'''

    return rx.card(
        rx.vstack(
            [
                rx.card(
                    rx.hstack(
                        rx.image(src=imagen, width="50%", height="auto"),
                        rx.divider(orientation="vertical", color="black", size="3", high="100%"),
                        rx.vstack(
                            rx.heading(header , size="6", align="left"),
                            rx.text(texto, align="left", text_align = "justify",),
                            rx.link("repositorio en GitHub", href=enlace, is_external=True),
                        ),
                    ),
                    box_shadow="lg",  # Agrega sombra para destacar el card
                    border_radius="10px",  # Opcional: redondea los bordes
                    padding_y=Size.MEDIUM.value,
                    margin_bottom = Size.VERY_BIG.value,
                    margin_y = Size.MEDIUM.value,
                    margin_x = Size.BIG.value,
                    max_width= MAX_WIDTH,
                    background_color=Color.PRIMARY.value,
                    width= "100%"  
                )
                for header, texto, enlace, imagen in zip(headers,textos, enlaces, imagenes)
            ]
        ),
        #align = "center",
        #padding_left=Size.MAX_BIG.value,  # Ajusta el padding del contenedor principal
        padding=Size.MEDIUM.value,  # Ajusta el padding del contenedor principal
        spacing=Size.MEDIUM.value,  # Ajusta el espaciado entre los cards
        width="100%",  # Asegúrate de que el contenedor ocupe todo el ancho
    )