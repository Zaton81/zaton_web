import reflex as rx
from zaton_web.parts.header import navbar
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
from zaton_web.parts.footer import footer
from zaton_web.parts.buttons import card_buttons
from zaton_web.parts.cards import card_portfolio

@rx.page(route= PORTFOLIO)
def portfolio() -> rx.Component:
    '''función index devuelve los componentes de la página de inicio'''
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Portfolio", size="9", align="left", margin_x = Size.SMALL.value),
            rx.text(TEXTO_PORTFOLIO1, weight="bold", margin_x = Size.BIG.value),
            rx.text(TEXTO_PORTFOLIO2,  rx.link("GitHub", href=GITHUB, is_external=True), margin_x = Size.BIG.value),    
            rx.center(
                rx.hstack(
                    card_portfolio(
                        headers= [TAREAS, PROYECTOS, VIDEOFLIX, PERSONAL],
                        textos = [TEXTO_TAREAS, TEXTO_PROYECTOS, TEXTO_VIDEOFLIX, TEXTO_PERSONAL],
                        enlaces = [APP_TAREAS, APP_PROYECTOS, APP_VIDEOFLIX, APP_PERSONAL],
                        imagenes = ["/tareas.png", "/proyectos.png", "/videoflix.png", "/webzaton.png"]
                    ),
                ),
            spacing=Spacing.SMALL.value,
            width="100%",
            padding_top=Size.BIG.value,
            padding_bottom=Size.MAX_BIG.value,
            #justify="center",
            ),
        ),
        footer(),
    )

