import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer
from zaton_web.parts.buttons import card_buttons
from zaton_web.parts.forms import contact_form

@rx.page(route= CONTACTO)
def contacto() -> rx.Component:
    '''función index devuelve los componentes de la página de inicio'''
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.hstack(
                rx.vstack(
                    rx.heading("Jorge Zatón Pérez", size="9", align="center"),
                    rx.heading(
                        LEMA, size="6"
                    ),
                    contact_form(),
                    spacing=Spacing.LARGE.value,
                    justify="center",
                    min_height="85vh",
                )
            )
        ),
        footer()
    )