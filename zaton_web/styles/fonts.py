'''archivo de fuentes y PESO de fuente de la web
'''
from enum import Enum

class Font(Enum):
    '''Clase Fuente, en él se incluyen las fuentes utilizadas en la web'''
    DEFAULT= "Poppins"
    SECONDARY="Roboto"
    ALTERNATIVE="Inter"

class FontWeight(Enum):
    '''Clase FontWeight
    Se encluye el peso de la fuente'''
    LIGHT = "300"
    MEDIUM = "500"