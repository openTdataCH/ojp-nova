from dataclasses import dataclass, field
from typing import Optional
from nova.klassen_typ_code import KlassenTypCode
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class KlassenTyp:
    """Der KlassenTyp enthält die Klassenspanne für den anfragenden
    Leistungsvermittler, das heisst die Menge aller wählbaren Klassen.

    Repräsentiert die Klasse, in der die Reise angetreten werden kann.
    Bspw. 1. Klasse oder 2. Klasse.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    code: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
