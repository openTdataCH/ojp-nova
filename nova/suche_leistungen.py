from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_such_request import LeistungsSuchRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class SucheLeistungen:
    class Meta:
        name = "sucheLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_such_request: Optional[LeistungsSuchRequest] = field(
        default=None,
        metadata={
            "name": "leistungsSuchRequest",
            "type": "Element",
            "required": True,
        }
    )
