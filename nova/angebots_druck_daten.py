from dataclasses import dataclass, field
from typing import List, Optional
from nova.druck_beleg import DruckBeleg

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsDruckDaten:
    beleg: List[DruckBeleg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
