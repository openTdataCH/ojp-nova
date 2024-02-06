from dataclasses import dataclass, field
from typing import Optional
from nova.haltestellen_verbund_daten_response import HaltestellenVerbundDatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetHaltestellenVerbundDatenResponse:
    class Meta:
        name = "getHaltestellenVerbundDatenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    haltestellen_verbund_daten_response: Optional[HaltestellenVerbundDatenResponse] = field(
        default=None,
        metadata={
            "name": "haltestellenVerbundDatenResponse",
            "type": "Element",
            "required": True,
        }
    )
