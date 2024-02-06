from dataclasses import dataclass, field
from typing import Optional
from nova.get_haltestellen_verbund_daten import GetHaltestellenVerbundDaten

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_haltestellen_verbund_daten: Optional[GetHaltestellenVerbundDaten] = field(
            default=None,
            metadata={
                "name": "getHaltestellenVerbundDaten",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
