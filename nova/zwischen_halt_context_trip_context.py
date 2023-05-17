from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class ZwischenHaltContextTripContext(Enum):
    PLANNED = "PLANNED"
    UNPLANNED = "UNPLANNED"
    IRRELEVANT = "IRRELEVANT"
    CANCELLED = "CANCELLED"
