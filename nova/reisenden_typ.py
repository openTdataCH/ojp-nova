from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString
from nova.reisenden_typ_code import ReisendenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ReisendenTyp:
    """
    Kennzeichnet den Typ des Reisenden (Person, Velo, etc.)
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    code: Optional[ReisendenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
