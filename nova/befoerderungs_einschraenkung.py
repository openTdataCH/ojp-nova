from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class BefoerderungsEinschraenkung(Enum):
    VELOBEFOERDERUNG_NICHT_ERLAUBT = "VELOBEFOERDERUNG_NICHT_ERLAUBT"
    VELOBEFOERDERUNG_NUR_INTERNATIONALER_VERKEHR = "VELOBEFOERDERUNG_NUR_INTERNATIONALER_VERKEHR"
    HUNDEBEFOERDERUNG_NICHT_ERLAUBT = "HUNDEBEFOERDERUNG_NICHT_ERLAUBT"
