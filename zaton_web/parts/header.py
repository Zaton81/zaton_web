import reflex as rx
from zaton_web.styles.styles import *
from zaton_web.styles.colors import Color
from zaton_web.styles.constants import HOME, BIO, LIBROS, CONTACTO, PORTFOLIO

def navbar_link(text: str, url: str) -> rx.Component:
    '''función nabvar_link
    retorna un componente para añadir enlaces al header o navbar'''
    return rx.link(
        rx.text(text, size=Spacing.BIG.value, weight="medium"), href=url
    )
def navbar() -> rx.Component:
    '''función navbar
    retorna un componente de reflex para dar forma a la cabecera principal (navbar) de la web'''
    return rx.hstack(
        rx.image(
            src="/logo2.svg",
            width=Size.VERY_BIG.value,
            height="auto",
            border_radius="10%",
        ),
        rx.link(
            rx.box(
                rx.heading("Jorge Zatón", as_="span", color=Color.SEC_CONTENT.value),
                style = HEADER_STYLE
            ),
            href=HOME
        ),
        rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Portfolio", PORTFOLIO),
                    navbar_link("Libros", LIBROS),
                    navbar_link("Biografía", BIO),
                    navbar_link("Contacto", CONTACTO),
                    spacing=Spacing.VERY_BIG.value,
                    justify = "end"
                    ),
        justify = "between",
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )