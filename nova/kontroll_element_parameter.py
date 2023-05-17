from dataclasses import dataclass, field
from typing import Optional
from nova.kontroll_element_format import KontrollElementFormat
from nova.sprach_code import SprachCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KontrollElementParameter:
    """
    :ivar sprache: Moegliche Werte: DE, EN, IT, FR
    :ivar format: Moegliche Werte: PNG, RAW
    """
    sprache: Optional[SprachCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    format: Optional[KontrollElementFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
