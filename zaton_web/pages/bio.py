import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer

@rx.page(route= BIO) 
def bio() -> rx.Component:
    '''función bio devuelve los componentes de la página de biografía'''
    # Bio Page
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Biografía", size="9", align="center"),
                rx.heading("Jorge Zatón Pérez", size="6", align="center"),
                rx.text(TEXTO_BIO)
            ),
        ),
        footer()
    )