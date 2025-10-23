from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoParamStructure:
    """
    TripInfo request parameter structure.

    :ivar use_timetabled_data_only: Do not show any realtime or incident
        data. Default is false.
    :ivar include_calls: Whether service pattern is to be included.
        Default is true.
    :ivar include_position: Whether current position is to be included.
        Default is true.
    :ivar include_service: Whether service information is to be
        included. Default is true.
    :ivar include_track_sections: Whether the result should include
        TrackSection elements to describe the geographic route of this
        vehicle journey.
    :ivar include_track_projection: Whether the result should include
        the geographic projection (coordinates) of this vehicle journey.
    :ivar extension:
    """
    use_timetabled_data_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseTimetabledDataOnly",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_position: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeService",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_track_sections: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTrackSections",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_track_projection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTrackProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
