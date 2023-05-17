from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_status import LeistungsStatus

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StornierungsInfo:
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
