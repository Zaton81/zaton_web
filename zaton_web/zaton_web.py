"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from zaton_web.pages.home import index
from zaton_web.pages.bio import bio
from zaton_web.pages.contacto import contacto
from zaton_web.pages.libros import libros
from zaton_web.pages.portfolio import portfolio
from zaton_web.pages.blog import blog
from zaton_web.styles.styles import BASE_STYLE



class State(rx.State):
    """The app state."""

    ...





app = rx.App(style=BASE_STYLE)

