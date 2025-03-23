import reflex as rx
from zaton_web.styles.colors import Color
from zaton_web.styles.styles import Spacing, Size


def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    '''función form_field recibe los parámetros 
    label, placeholder, type y name y devuelve un componente de un iput para añadir a un formulario'''
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type,
                    background_color=Color.BACKGROUND.value,
                ),
                as_child=True,
            ),
            direction="column",
            spacing=Spacing.VERY_SMALL.value,
        ),
        name=name,
        width="100%",
    )


def contact_form() -> rx.Component:
    '''función contact_form 
    retorna un formulario de contacto'''
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="orange",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Envíame un mensaje",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Rellena el formulario y me pondré en contacto contigo lo antes posible.",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing=Spacing.DEFAULT.value,
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Nombre",
                            "Nombre",
                            "text",
                            "Nombre",
                        ),
                        form_field(
                            "Apellidos",
                            "Apellidos",
                            "text",
                            "Apellidos",
                        ),
                        spacing=Spacing.SMALL.value,
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "correo electrónico",
                            "tucorreo@tuemail.com",
                            "email",
                            "email",
                        ),
                        form_field(
                            "Teléfono", "Teléfono", "tel", "Teléfono"
                        ),
                        spacing=Spacing.SMALL.value,
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Mensaje",
                            name="Mensaje",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing=Spacing.VERY_SMALL.value,
                    ),
                    rx.form.submit(
                        rx.button("Enviar mensaje"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing=Spacing.SMALL.value,
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing=Spacing.DEFAULT.value,
        ),
        size="3",
    )