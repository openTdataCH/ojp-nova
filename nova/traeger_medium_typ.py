from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class TraegerMediumTyp:
    """Medium, auf dem die für die Kontrolle und den Kunden relevanten
    Informationen aufgedruckt bzw.

    angezeigt werden. Das Medium kann in physischer oder elektronischer
    Form sein.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    beschreibung_screen: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "beschreibungScreen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    beschreibung_ausgabe: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "beschreibungAusgabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
