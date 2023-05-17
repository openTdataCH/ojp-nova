from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class Haltestelle:
    """Entspricht einem Knoten im Verkehrsnetz.

    Wird verwendet um den Weg eines Verkehrsangebots zu beschreiben.
    """
    bav_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "bavName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 64,
        }
    )
    koordinate_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "koordinateX",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    koordinate_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "koordinateY",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    uic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "uicCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )
