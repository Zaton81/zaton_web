"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from zaton_web.pages import home
from zaton_web.styles.styles import BASE_STYLE


class State(rx.State):
    """The app state."""

    ...





app = rx.App(style=BASE_STYLE)

