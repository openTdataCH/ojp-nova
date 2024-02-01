from dataclasses import dataclass, field
from typing import Optional
from nova.haltestellen_verbund_daten_request import HaltestellenVerbundDatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetHaltestellenVerbundDaten:
    class Meta:
        name = "getHaltestellenVerbundDaten"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    haltestellen_verbund_daten_request: Optional[HaltestellenVerbundDatenRequest] = field(
        default=None,
        metadata={
            "name": "haltestellenVerbundDatenRequest",
            "type": "Element",
            "required": True,
        }
    )
