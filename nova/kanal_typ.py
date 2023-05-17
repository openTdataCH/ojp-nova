from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


class KanalTyp(Enum):
    AUTOMAT = "AUTOMAT"
    ONLINE = "ONLINE"
    BEDIENTER_VERKAUF = "BEDIENTER_VERKAUF"
    BATCH = "BATCH"
