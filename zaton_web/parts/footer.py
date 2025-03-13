import reflex as rx
from zaton_web.styles.styles import *
from zaton_web.styles.colors import Color
from zaton_web.styles.constants import HOME
import datetime

def footer() ->rx.Component:
    '''funcion footer
    retorna un componente de reflex para dar forma al footer principal de la web'''
    return rx.vstack(
        rx.text(
            #datetime.now.year(),
            f"{datetime.date.today().year} Todos los derechos reservados. Web construida por Jorge Zatón Pérez como proyecto final del curso de Python de ",
            rx.link(
                "Tokio School.",
                    href="https://tokioschool.com/",
                    is_external=True,
                    color_scheme="orange"
            )
        ),
        style=FOOTER_STYLE,
        position="bottom",
        bottom="0",
        font_family=Font.SECONDARY.value
    )