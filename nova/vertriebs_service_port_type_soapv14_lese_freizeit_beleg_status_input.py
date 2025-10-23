from dataclasses import dataclass, field
from typing import Optional
from nova.lese_freizeit_beleg_status import LeseFreizeitBelegStatus

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        lese_freizeit_beleg_status: Optional[LeseFreizeitBelegStatus] = field(
            default=None,
            metadata={
                "name": "leseFreizeitBelegStatus",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
