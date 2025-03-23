import reflex as rx
from zaton_web.styles.styles import *
from zaton_web.styles.colors import Color
from zaton_web.styles.constants import *
import datetime

def footers() ->rx.Component:
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

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)



def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href, is_external=True)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", INSTAGRAM),
        social_link("twitter", TWITTER),
        social_link("facebook", FACEBOOK),
        social_link("linkedin", LINKEDIN),
        social_link("github", GITHUB),
        spacing="3",
        justify_content=["center", "center", "end"],
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width=Size.BIG.value,
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        f"© {datetime.date.today().year} Todos los derechos reservados. Web construida por ",
                            rx.link(
                                "Jorge Zatón Pérez.",
                                href=WEB_PERSONAL,
                                is_external=True,
                                color_scheme="orange"
                            ),
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        style = FOOTER_STYLE,
                        font_color=Color.BACKGROUND.value
                    ),
                    spacing=Spacing.SMALL.value,
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                socials(),
                spacing=Spacing.DEFAULT.value,
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing=Spacing.LARGE.value,
            width="100%",
            eight="100%",
        ),
        width="100%",
        padding_x = Size.SMALL.value,
        padding_bottom= Size.DEFAULT.value,
        style=FOOTER_STYLE,
        bottom=Spacing.ZERO.value,
        z_index= "1000",
        position="fixed",  
        font_family=Font.SECONDARY.value,
    )