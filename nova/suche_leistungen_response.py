from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_such_response import LeistungsSuchResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class SucheLeistungenResponse:
    class Meta:
        name = "sucheLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_such_response: Optional[LeistungsSuchResponse] = field(
        default=None,
        metadata={
            "name": "leistungsSuchResponse",
            "type": "Element",
            "required": True,
        }
    )
