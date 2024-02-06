from dataclasses import dataclass, field
from typing import List, Optional
from nova.localized_text import LocalizedText
from nova.localized_url import LocalizedUrl

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class InfoText:
    """
    :ivar info_link:
    :ivar info_text:
    :ivar produkt_nummern: Verweist auf die ProduktNummern, für die
        dieser Infotext zutreffend ist.
    :ivar info_text_id: StammdatenId, auf die von VertriebService
        Antworten verwiesen wird (z.B. AngebotsAntwort)
    :ivar kategorie: Unterscheidet, ob Infotexte nur Kundenberater*innen
        oder auch Endkunden angezeigt werden sollen.
    """
    info_link: Optional[LocalizedUrl] = field(
        default=None,
        metadata={
            "name": "infoLink",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    info_text: Optional[LocalizedText] = field(
        default=None,
        metadata={
            "name": "infoText",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    produkt_nummern: Optional["InfoText.ProduktNummern"] = field(
        default=None,
        metadata={
            "name": "produktNummern",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    info_text_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "infoTextId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    kategorie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )

    @dataclass
    class ProduktNummern:
        produkt_nummer: List[int] = field(
            default_factory=list,
            metadata={
                "name": "produktNummer",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "min_occurs": 1,
                "min_inclusive": 0,
            }
        )
