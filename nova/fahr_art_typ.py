from dataclasses import dataclass, field
from typing import Optional
from nova.fahr_art_typ_code import FahrArtTypCode
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class FahrArtTyp:
    """
    Ein FahrartTyp kann sein Einfach, Retour oder Rundfahrt.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    code: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
