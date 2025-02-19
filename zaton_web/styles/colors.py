'''archivo en el que se incluyen los colores genéricos de la web'''

from enum import Enum
import reflex as rx

class Color(Enum):
    PRIMARY = "#1E3A8A" #azul oscuro
    SECONDARY = "#FFFFFF" #blanco, para fondos
    BACKGROUND = "#F3F4F6" #gris claro, contenidos secundarios y fondos
    CONTENT = "#F97316" #naranja, cbotones y contenidos destacados 
    PURPLE = "#10B981" #verde esmeralda, alternativo 
    BUTTON = "cyan"