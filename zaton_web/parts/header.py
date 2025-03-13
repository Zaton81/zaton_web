import reflex as rx
from zaton_web.styles.styles import *
from zaton_web.styles.colors import Color
from zaton_web.styles.constants import HOME

def navbar() -> rx.Component:
    '''función navbar
    retorna un componente de reflex para dar forma a la cabecera principal (navbar) de la web'''
    return rx.hstack(
        rx.link(
            rx.box(
                rx.heading("Jorge Zatón", as_="span", color=Color.SEC_CONTENT.value),
                style = HEADER_STYLE
            ),
            href=HOME
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )