from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString
from nova.verkehrs_mittel_typ_code import VerkehrsMittelTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VerkehrsMittelTyp:
    """
    Ein VerkehrsMittel beschreibt ein bewegliches Transportmittel wie Zug, Schiff,
    Bus, Tram oder Seilbahn, welches Personen transportiert.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    code: Optional[VerkehrsMittelTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
