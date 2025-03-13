import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer
from zaton_web.parts.buttons import card_buttons

@rx.page(route= HOME)
def index() -> rx.Component:
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
                    rx.link(
                        rx.button("Check out our docs!"),
                        href="https://reflex.dev/docs/getting-started/introduction/",
                        is_external=True,
                    ),
                    spacing=Spacing.LARGE.value,
                    justify="center",
                    min_height="85vh",
                ),
                rx.divider(orientation="vertical", color=Color.TEXTO.value, size="3", high="100%"),
                rx.vstack(
                    card_buttons(
                        textos=["Portfolio", "Biografía", "Contacto", "Libros"],
                        enlaces = [PORTFOLIO, BIO, CONTACTO, LIBROS],
                        iconos = ["briefcase_business", "user-pen", "mail", "book_text"]))
            )
        ),
        footer()
    )