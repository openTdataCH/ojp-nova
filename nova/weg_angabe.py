from dataclasses import dataclass, field
from typing import List, Optional
from nova.reise_route_segment import ReiseRouteSegment
from nova.tarif_klasse import TarifKlasse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class WegAngabe:
    """
    Die Wegangabe beschreibt die tarifarische Gültigkeit in textueller Form und
    wird zu Kontrollzwecken aufs Ticket aufgedruckt.
    """
    abgang: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    bestimmung: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    reise_route_segment: List[ReiseRouteSegment] = field(
        default_factory=list,
        metadata={
            "name": "reiseRouteSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    tarif_klasse: Optional[TarifKlasse] = field(
        default=None,
        metadata={
            "name": "tarifKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
