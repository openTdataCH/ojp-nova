from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from ojp2.stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopFareRequestStructure:
    """Sub-request: stop-related fare information.

    :ivar stop_point_ref: Reference to the stop point.
    :ivar date: Date for which to retrieve Fare information.
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
