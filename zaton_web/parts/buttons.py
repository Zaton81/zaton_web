import reflex as rx
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *


def card_buttons(textos=[], enlaces=[], iconos=[]) -> rx.Component:
    '''Función que devuelve un conjunto de botones en un card
    textos: lista de textos de los botones
    enlaces: lista de enlaces a los que llevan los botones'''

    return rx.card(
        rx.vstack(
            [
                rx.link(
                    rx.card(
                        rx.icon(icono, size=50),  # Ajusta el tamaño del ícono si es necesario
                        texto,
                        width="90%",  # Ajusta el ancho del card
                        height="auto",  # Ajusta la altura del card
                        padding=Size.MEDIUM.value,  # Aumenta el padding interno
                        box_shadow="lg",  # Agrega sombra para destacar el card
                        border_radius="10px",  # Opcional: redondea los bordes
                    ),
                    href=enlace,
                    width="100%",  # Asegúrate de que el enlace ocupe todo el espacio
                )
                for texto, enlace, icono in zip(textos, enlaces, iconos)
            ]
        ),
        padding=Size.MEDIUM.value,  # Ajusta el padding del contenedor principal
        spacing=Size.MEDIUM.value,  # Ajusta el espaciado entre los cards
        width="100%",  # Asegúrate de que el contenedor ocupe todo el ancho
    )