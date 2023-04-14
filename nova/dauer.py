from dataclasses import dataclass, field
from typing import Optional
from nova.zeit_einheit import ZeitEinheit

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Dauer:
    """
    Aggregation von Wert und Einheit.
    """
    wert: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_inclusive": 0,
        }
    )
    einheit: Optional[ZeitEinheit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
