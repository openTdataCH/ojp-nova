from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ErmaessigungsKarte:
    """Medium, auf dem die für die Kontrolle und den Kunden relevanten
    Informationen aufgedruckt bzw.

    angezeigt werden. Das Medium kann in physischer oder elektronischer
    Form sein.
    """
    ermaessigungs_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "ermaessigungsBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    ermaessigungs_karte_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ermaessigungsKarteCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
