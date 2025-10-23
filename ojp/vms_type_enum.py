from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class VmsTypeEnum(Enum):
    COLOUR_GRAPHIC = "colourGraphic"
    CONTINUOUS_SIGN = "continuousSign"
    MONOCHROME_GRAPHIC = "monochromeGraphic"
    OTHER = "other"
