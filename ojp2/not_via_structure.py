from dataclasses import dataclass, field
from typing import Optional

from ojp2.stop_place_ref_2 import StopPlaceRef2
from ojp2.stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class NotViaStructure:
    """
    Not-via restrictions for a TRIP, i.e. SCHEDULED STOP POINTs or STOP PLACEs that
    the TRIP is not allowed to pass through.

    :ivar stop_point_ref: Reference to a not-via stop point.
    :ivar stop_place_ref: Reference to a not-via stop place.
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRef2] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
