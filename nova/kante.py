from dataclasses import dataclass, field
from typing import Optional
from nova.verkehrs_mittel_typ_code import VerkehrsMittelTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Kante:
    """
    Eine Kante verbindet zwei Haltestellen im Verkehrsnetz.
    """
    von: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    nach: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verkehrs_mittel_typ: Optional[VerkehrsMittelTypCode] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
