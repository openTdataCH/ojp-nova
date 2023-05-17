from dataclasses import dataclass, field
from typing import Optional
from ojp.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ServiceViaPointStructure:
    """[a specialisation of VIA in TMv6] STOP PLACE or SCHEDULED STOP POINT as a
    VIA for a particular SERVICE PATTERN.

    Specialisation of a VIA.

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
    :ivar display_priority: Priority of this via point to be displayed
        when space is limited.
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
    display_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayPriority",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_inclusive": 1,
            "max_inclusive": 5,
        }
    )
