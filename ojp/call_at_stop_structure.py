from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.international_text_structure import InternationalTextStructure
from ojp.situation_full_ref_2 import SituationFullRef2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class CallAtStopStructure:
    """
    [same as CALL in SIRI] the meeting of a VEHICLE JOURNEY with a specific
    SCHEDULED STOP POINT.

    :ivar stop_point_ref:
    :ivar stop_point_name: Name or description of stop point for use in
        passenger information.
    :ivar name_suffix: Additional description of the stop point that may
        be appended to the name if enough space is available. F.e.
        "opposite main entrance".
    :ivar planned_quay: Name of the bay where to board/alight from the
        vehicle. According to planned timetable.
    :ivar estimated_quay: Name of the bay where to board/alight from the
        vehicle. As to the latest realtime status.
    :ivar service_arrival: Arrival times of the service at this stop (
        group of attributes of TIMETABLED PASSING TIME, ESTIMATED
        PASSING TIME, OBSERVED PASSING TIME).
    :ivar service_departure: Departure times of the service at this stop
        ( group of attributes of TIMETABLED PASSING TIME, ESTIMATED
        PASSING TIME, OBSERVED PASSING TIME).
    :ivar order: Sequence number of this stop in the service pattern of
        the journey.
    :ivar request_stop: The vehicle journey calls at this stop only on
        demand.
    :ivar unplanned_stop: This stop has not been planned by the planning
        department.
    :ivar not_serviced_stop: The vehicle will not call at this stop
        despite earlier planning.
    :ivar situation_full_ref:
    """
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_point_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    planned_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PlannedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    estimated_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "EstimatedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    service_arrival: Optional["CallAtStopStructure.ServiceArrival"] = field(
        default=None,
        metadata={
            "name": "ServiceArrival",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    service_departure: Optional["CallAtStopStructure.ServiceDeparture"] = field(
        default=None,
        metadata={
            "name": "ServiceDeparture",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    unplanned_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnplannedStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    not_serviced_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NotServicedStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    situation_full_ref: List[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )

    @dataclass
    class ServiceArrival:
        """
        :ivar timetabled_time: time at point as it is published
        :ivar recorded_at_time: time as it was recorded
        :ivar estimated_time: estimated time (for prognosis)
        :ivar estimated_time_low: Estimated lower limit for time.
        :ivar estimated_time_high: Estimated upper limit for time.
        """
        timetabled_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "TimetabledTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "required": True,
            }
        )
        recorded_at_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "RecordedAtTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time_low: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTimeLow",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time_high: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTimeHigh",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )

    @dataclass
    class ServiceDeparture:
        """
        :ivar timetabled_time: time at point as it is published
        :ivar recorded_at_time: time as it was recorded
        :ivar estimated_time: estimated time (for prognosis)
        :ivar estimated_time_low: Estimated lower limit for time.
        :ivar estimated_time_high: Estimated upper limit for time.
        """
        timetabled_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "TimetabledTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "required": True,
            }
        )
        recorded_at_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "RecordedAtTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTime",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time_low: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTimeLow",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
        estimated_time_high: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EstimatedTimeHigh",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            }
        )
