from dataclasses import dataclass, field
from typing import List, Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class TaxonomieKlasse:
    """
    :ivar bezeichnung: Lokalisierte Bezeichnung der Klasse (zur Anzeige)
    :ivar sub_taxonomie_klasse:
    :ivar produkt_nummer: Produkte, die dieser TaxonomieKlasse
        zugeordnet sind.
    :ivar name: Eindeutiger Klassenname
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    sub_taxonomie_klasse: List["TaxonomieKlasse"] = field(
        default_factory=list,
        metadata={
            "name": "subTaxonomieKlasse",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    produkt_nummer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "produktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
