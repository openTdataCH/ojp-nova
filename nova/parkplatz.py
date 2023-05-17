from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class Parkplatz:
    """
    Repräsentiert Element Parkplatz  (ParkplatzCode und Bezeichnung)
    """
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    parkplatz_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkplatzCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999999,
        }
    )
