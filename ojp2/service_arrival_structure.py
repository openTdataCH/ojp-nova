from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.arrival_formation_assignment import ArrivalFormationAssignment

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ServiceArrivalStructure:
    """
    Arrival times of a service at a stop (group of attributes of TIMETABLED PASSING
    TIME, ESTIMATED PASSING TIME, OBSERVED PASSING TIME, equals MONITORED LEG
    ARRIVAL).

    :ivar timetabled_time: time at point as it is published
    :ivar recorded_at_time: time as it was recorded
    :ivar estimated_time: estimated time (for prognosis)
    :ivar estimated_time_low: Estimated lower limit for time.
    :ivar estimated_time_high: Estimated upper limit for time.
    :ivar arrival_formation_assignment:
    """

    timetabled_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimetabledTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    estimated_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EstimatedTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    estimated_time_low: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EstimatedTimeLow",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    estimated_time_high: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EstimatedTimeHigh",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    arrival_formation_assignment: list[ArrivalFormationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFormationAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
