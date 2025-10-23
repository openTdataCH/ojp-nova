from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class WegPosition(Enum):
    ANFANG = "ANFANG"
    UNTERWEGS = "UNTERWEGS"
    ENDE = "ENDE"
