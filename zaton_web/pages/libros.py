import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer
from zaton_web.parts.buttons import card_buttons

@rx.page(route= LIBROS)
def libros() -> rx.Component:
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
                    rx.text(TEXTO_LIBROS_PAGE, text_align="justify"),
                    rx.image(src="/zaton_pajarita.svg", max_height = Size.IMAGE.value, width="auto"),
                    spacing=Spacing.LARGE.value,
                    justify="center",
                    padding_x = Size.MEDIUM.value,
                    min_height="85vh",
                    width = "45%"
                ),
                rx.divider(orientation="vertical", color=Color.TEXTO.value, size="3", height="100%"),
                rx.vstack(
                    rx.hstack(
                        rx.image(src="/quiza_lo_quiso_portada.png", width= Size.IMAGE.value, height="auto"),
                        rx.vstack(
                            rx.text(SINOPSIS_QUIZA,
                                    text_align = "justify",
                            ),
                            rx.link(
                                rx.button("Cómprame", width = "100%"),
                                href= AMAZON_QUIZA,
                                is_external= True,
                                width = "100%"
                            )
                        )
                    ),
                    rx.divider(color_scheme= "purple", margin_y= Size.MEDIUM.value),
                    rx.hstack(
                        rx.image(src="/Con_todo_portada.png", width= Size.IMAGE.value, height="auto"),
                        rx.vstack(
                            rx.text(SINOPSIS_CONTRA,
                                    text_align = "justify",
                            ),
                            rx.link(
                                rx.button("Cómprame", width = "100%"),
                                href= AMAZON_CONTRA,
                                is_external= True,
                                width = "100%"
                            ),
                            padding_y = Size.BIG.value
                        ),
                    ),
                    padding_y = Size.VERY_BIG.value,
                    width = "45%"
                ),
                height = "100%"
            ),
            
        ),
        footer()
    )