import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import MAX_WIDTH, Size, Spacing
from zaton_web.styles.colors import Color
from zaton_web.parts.footer import footer

@rx.page(route= BIO) 
def bio() -> rx.Component:
    '''función bio devuelve los componentes de la página de biografía'''
    # Bio Page
    return rx.box(
        navbar(),
        rx.vstack(
        rx.heading("Biografía", size="9", align="left"),
        rx.heading("Jorge Zatón Pérez", size="6", align="left"),
        padding_x = Size.MEDIUM.value
        ),
        rx.divider(color_scheme= "purple", margin_y= Size.MEDIUM.value),
        rx.center(
            rx.vstack(
                rx.text(PARRAFO_BIO1),
                rx.text(PARRAFO_BIO2),
                rx.text(PARRAFO_BIO3),
                rx.heading(HABILIDADES, size="4", weight="bold"),
                rx.text(PARRAFO_BIO4),
                rx.text(PARRAFO_BIO5),
                rx.text(PARRAFO_BIO6),
                rx.heading(FILOSOFIA, size="4", weight="bold"),
                rx.text(PARRAFO_BIO7),
                rx.text(PARRAFO_BIO8),
                rx.text(PARRAFO_BIO9),
                rx.text(PARRAFO_BIO10),
                rx.text(CITA, weight="bold"),
                rx.heading(TEXTO_LIBROS, size= "4", weight="bold"),
                rx.text(PARRAFO_LIBROS),
                max_width = MAX_WIDTH,
                spacing = Spacing.LARGE.value,
                text_align = "justify",
                padding_bottom = Size.MAX_BIG.value
            ),
        ),
        footer(),
    )