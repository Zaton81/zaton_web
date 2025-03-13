import reflex as rx
from zaton_web.styles.constants import *
from zaton_web.styles.styles import *
def card_buttons(textos= [], enlaces= [], iconos = []) -> rx.Component:
    '''función que devuelve un conjunto de botones en un card
    textos: lista de textos de los botones
    enlaces: lista de enlaces a los que llevan los botones'''

    return rx.card(
        rx.vstack(
        [rx.link(
            rx.card(
                rx.icon(icono),
                texto,),
            href=enlace) 
            for texto, enlace, icono in zip(textos, enlaces, iconos)]
        ),
            
        padding=Size.SMALL.value,
        spacing=Size.SMALL.value,
        width="100%"
    )