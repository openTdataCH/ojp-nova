from dataclasses import dataclass, field
from typing import List, Optional
from nova.fahrplan_verbindungs_segment import FahrplanVerbindungsSegment
from nova.strecke import Strecke

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FahrplanVerbindung(Strecke):
    """
    Eine Verbindungsanfrage beschreibt eine Kundenanfrage für eine Angebotsanfrage
    anhand Verbindungsinformationen aus dem Fahrplan.
    """
    verbindungs_segment: List[FahrplanVerbindungsSegment] = field(
        default_factory=list,
        metadata={
            "name": "verbindungsSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
