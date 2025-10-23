from dataclasses import dataclass, field
from typing import List, Optional
from nova.taxonomie_klasse import TaxonomieKlasse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ProduktTaxonomie:
    """
    :ivar klasse:
    :ivar leistungs_vermittler: Liste aller Leistungsvermittler, die
        diese Taxonomie verwenden.
    :ivar name: Eindeutiger Name der ProduktTaxonomie
    """
    klasse: List[TaxonomieKlasse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    leistungs_vermittler: Optional["ProduktTaxonomie.LeistungsVermittler"] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
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

    @dataclass
    class LeistungsVermittler:
        partner_code: List[int] = field(
            default_factory=list,
            metadata={
                "name": "partnerCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "max_inclusive": 99999,
            }
        )
