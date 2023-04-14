from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GruppenReiseInfoRequest:
    """
    :ivar anzahl:
    :ivar kunden_segment_code:
    :ivar ist_reise_leiter_kunden_segment: @Deprecated Will be removed
        in NOVA 15.
    """
    anzahl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
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
    ist_reise_leiter_kunden_segment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istReiseLeiterKundenSegment",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
