from dataclasses import dataclass, field
from typing import List, Optional
from nova.fahrplan_verbindungs_segment import FahrplanVerbindungsSegment

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class VerbindungPreisAuskunft:
    segment_hin_fahrt: List[FahrplanVerbindungsSegment] = field(
        default_factory=list,
        metadata={
            "name": "segmentHinFahrt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
