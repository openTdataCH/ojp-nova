from dataclasses import dataclass, field
from typing import List, Optional
from nova.reise_route_segment import ReiseRouteSegment
from nova.strecken_weg_meta_daten import StreckenWegMetaDaten

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ReiseWegInfo:
    """Die Reiseroute setzt sich aus mehreren geordneten ReiserouteSegmenten
    zusammen.

    Die Summe aller aneinandergereihter Segmente ergibt die Beschreibung
    einer Reiseroute.
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
    strecken_weg_meta_daten: Optional[StreckenWegMetaDaten] = field(
        default=None,
        metadata={
            "name": "streckenWegMetaDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
