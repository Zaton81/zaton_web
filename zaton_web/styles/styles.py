'''archivo de estilado de la web. 
En él se crean los estilos por defecto (fondo, fuente, etc)'''
from enum import Enum
from .fonts import *
from .colors import *

# Constants
MAX_WIDTH = "600px"

class Size(Enum):
    '''tamaños de la web para márgenes'''
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    MAX_BIG = "6em"
    IMAGE = "30em"



class Spacing(Enum):
    '''clase Spacing
    devuelve los distintos tamaños de spaciado'''
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

#estilo base de la web
        
#cabecera
HEADER_STYLE= {
    "font_family": Font.SECONDARY.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.PRIMARY.value
}
#principal
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": Color.TEXTO.value,
        "font_family": Font.SECONDARY.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": Color.PRIMARY.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SEC_CONTENT.value
        }
    },
    rx.link: {
        "color": Color.CONTENT.value,
        "text_decoration": "none",
        "_hover": {}
    }
}
FOOTER_STYLE= {
    "font_family": Font.SECONDARY.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.PRIMARY.value,
    "font_color" : Color.BACKGROUND.value,
    "color" : Color.BACKGROUND.value
}

#video
VIDEO_STYLE = {
    "width": "720px",
    
    "eight" : "auto"
}