from dataclasses import dataclass, field
from typing import Optional

from ojp2.include_formation_enumeration import IncludeFormationEnumeration
from ojp2.use_realtime_data_enumeration import UseRealtimeDataEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoParamStructure:
    """
    TripInfo request parameter structure.

    :ivar use_real_time_data: Use real-time data. Default is "full"
    :ivar include_calls: Whether call information is to be included.
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
    :ivar include_places_context: Whether the place context is needed.
        If a requestor has that information already, the response can be
        made slimmer, when set to false. Default is true.
    :ivar include_formation: Whether the formation should be included.
        With "simple" only VehicleFeature is used. "full" may unleash
        the full power of the SIRI formation model (especially for
        trains). The OJP specification document gives hints on how to
        limit oneself as a server to the most important aspects. Default
        is none.
    :ivar include_situations_context: Whether the situation context is
        needed. If a requestor has that information by other means or
        can't process it, the response can be made slimmer, when set to
        false. Default is true
    :ivar extension:
    """

    use_real_time_data: Optional[UseRealtimeDataEnumeration] = field(
        default=None,
        metadata={
            "name": "UseRealTimeData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_position: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeService",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_track_sections: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTrackSections",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_track_projection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTrackProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_places_context: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePlacesContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_formation: Optional[IncludeFormationEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludeFormation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_situations_context: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituationsContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
