from dataclasses import dataclass, field
from typing import Optional
from nova.get_leistungs_status import GetLeistungsStatus

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14GetLeistungsStatusInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14GetLeistungsStatusInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        get_leistungs_status: Optional[GetLeistungsStatus] = field(
            default=None,
            metadata={
                "name": "getLeistungsStatus",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
