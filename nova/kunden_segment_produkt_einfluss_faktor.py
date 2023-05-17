from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KundenSegmentProduktEinflussFaktor:
    """
    Beschreibt als Spezialisierung eines Produkteinflussfaktors ein spezifisches
    KundenSegment (1/1, ?, Erwachsene, Ermassigt).

    :ivar bezeichnung:
    :ivar kunden_segment_code: Code kann über Stammdaten zu den
        relevanten Attributen (min/max Alter, reisendenTyp,
        ermaessigungsKarte etc.) aufgelöst werden.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kunden_segment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenSegmentCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
