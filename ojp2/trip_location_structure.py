from dataclasses import dataclass, field
from typing import Optional

from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.journey_ref import JourneyRef
from ojp2.line_ref_structure import LineRefStructure
from ojp2.operating_day_ref import OperatingDayRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripLocationStructure:
    """A trip location represents the current logical position of a journey
    service.

    It can be used similarly to a place e.g., for starting a new trip
    request from within this service. A trip location does not(!)
    describe the relative position of a traveller within a vehicle,
    e.g., the seat.

    :ivar operating_day_ref:
    :ivar journey_ref:
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
    """

    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
