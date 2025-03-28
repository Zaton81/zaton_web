import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer
from zaton_web.parts.buttons import card_buttons

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
                    rx.text("Si quieres ponerte en contacto conmigo, bien sea para trabajar juntos, proponerme un proyecto, ofrecerme empleo o comprar alguno de los libros, envíame un correo electrónico:"),
                    rx.link(
                        rx.button(
                            rx.icon("mail"),
                            "Enviar correo",
                            width="100%",
                            max_width= MAX_WIDTH
                        ),
                        href="mailto:zaton81@hotmail.com?subject=Contacto desde la web&body=Hola Jorge, me gustaría ponerme en contacto contigo.",
                        is_external=True,
                    ),
                    card_buttons(
                        textos=["Portfolio", "Biografía", "Contacto", "Libros"],
                        enlaces = [PORTFOLIO, BIO, CONTACTO, LIBROS],
                        iconos = ["briefcase_business", "user-pen", "mail", "book_text"]
                    ),
                    
                    spacing=Spacing.LARGE.value,
                    justify="center",
                    min_height="85vh",
                )
            )
        ),
        footer()
    )