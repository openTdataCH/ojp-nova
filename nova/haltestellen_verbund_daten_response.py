from dataclasses import dataclass, field
from typing import List
from nova.haltestellen_verbund_daten import HaltestellenVerbundDaten
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class HaltestellenVerbundDatenResponse(VertriebsStammdatenResponse):
    haltestellen_verbund_daten: List[HaltestellenVerbundDaten] = field(
        default_factory=list,
        metadata={
            "name": "haltestellenVerbundDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
