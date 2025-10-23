from dataclasses import dataclass, field
from typing import Optional
from nova.kunden_segment_produkt_einfluss_faktor import KundenSegmentProduktEinflussFaktor
from nova.preis import Preis

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ReiseGruppeInfo:
    preis_pro_reisender: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "preisProReisender",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kunden_segment: Optional[KundenSegmentProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "kundenSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    anzahl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
        }
    )
    anzahl_gratis: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlGratis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
        }
    )
