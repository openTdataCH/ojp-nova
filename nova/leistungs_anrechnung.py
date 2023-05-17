from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistungs_info_type import LeistungsInfoType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsAnrechnung:
    leistungs_info: Optional[LeistungsInfoType] = field(
        default=None,
        metadata={
            "name": "leistungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    angerechnete_zone: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angerechneteZone",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
