from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class NotViaStructure:
    """
    NNot-via restrictions for a TRIP, i.e. SCHEDULED STOP POINTs or STOP PLACEs
    that the TRIP is not allowed to pass through.
    """
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
