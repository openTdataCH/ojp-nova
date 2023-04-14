from dataclasses import dataclass, field
from typing import Optional
from nova.verkehrs_kanten_sequenz import VerkehrsKantenSequenz
from nova.weg_position import WegPosition

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class TeilStrecke:
    teil_strecke: Optional[VerkehrsKantenSequenz] = field(
        default=None,
        metadata={
            "name": "teilStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    weg_position: Optional[WegPosition] = field(
        default=None,
        metadata={
            "name": "wegPosition",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
