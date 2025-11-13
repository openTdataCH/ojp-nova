from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.hierarchy_enumeration import HierarchyEnumeration
from ojp2.line_direction_filter_structure import LineDirectionFilterStructure
from ojp2.mode_filter_structure import ModeFilterStructure
from ojp2.operator_filter_structure import OperatorFilterStructure
from ojp2.stop_event_type_enumeration import StopEventTypeEnumeration
from ojp2.use_realtime_data_enumeration import UseRealtimeDataEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventParamStructure:
    """
    Request specific parameters (parameters which define what is to be included in
    a Stop  Event result)

    :ivar mode_filter: MODEs to be excluded or included in stop events.
        We on purpose don't use ModeOfOperationFilter in the stop event
        service.
    :ivar line_filter: Lines/Directions to include/exclude.
    :ivar operator_filter: Transport operators to include/exclude.
    :ivar include_all_restricted_lines: There might exist lines that
        have special restrictions and are not generally available to the
        public. E.g. school buses, company shuttles. dragLifts need to
        have an ACCESS MODE ski. Lines with ACCESS MODE bicycle will be
        included as well. If this flag is set, then existing restricted
        lines are considered by the router. The results are marked as
        restricted in the ServiceGroup. The usage could also be detailed
        with Attribute elements.
    :ivar number_of_results: parameter to control the number of TRIP
        results before/after a point in time. May NOT be used when
        departure time at origin AND arrival time at destination are set
    :ivar time_window: Time window events should lie within. Starting
        from time given in PlaceContext.
    :ivar stop_event_type: Only departures or arrivals or both.
    :ivar include_previous_calls: Whether the previous calls of each
        vehicle journey should be included in the response.
    :ivar include_onward_calls: Whether the onward calls of each vehicle
        journey should be included in the response.
    :ivar include_operating_days: Whether operating day information of
        this stop event should be included in the response.
    :ivar use_realtime_data: Whether real-time information of this stop
        event should be used in the response. Default is "full"
    :ivar include_places_context: Whether the place context is needed.
        If a requestor has that information already, the response can be
        made slimmer, when set to false. Default is true.
    :ivar include_situations_context: Whether the situation context is
        needed. If a requestor has that information by other means or
        can't process it, the response can be made slimmer, when set to
        false. Default is true
    :ivar include_stop_hierarchy: Indicates for which parts of the
        hierarchy of the StopPlace(s) stop events should be provided (if
        known by the server). "local" (default) is the local server
        setting. "no" will include no hierarchy and only provide the
        given StopPlace / StopPoint. "down" will include all lower
        StopPoints/ StopPlaces in the hierarchy, if such a hierarchy
        exists. "all" does include all StopPoints/StopPlaces for the
        meta station if it is known. How to use this: if you indicate
        the reference to a train station and the parameter is set to
        "down", the departures/arrivals at the associated bus stations
        will show as well. If you have the ScheduledStopPoint of
        platform B of the local bus and it is associated with 3 other
        stations, you will get all these arrivals/departures as well if
        the parameter is set to "all".
    :ivar extension:
    """

    mode_filter: Optional[ModeFilterStructure] = field(
        default=None,
        metadata={
            "name": "ModeFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    line_filter: Optional[LineDirectionFilterStructure] = field(
        default=None,
        metadata={
            "name": "LineFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operator_filter: Optional[OperatorFilterStructure] = field(
        default=None,
        metadata={
            "name": "OperatorFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_all_restricted_lines: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAllRestrictedLines",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    number_of_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResults",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    time_window: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeWindow",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stop_event_type: Optional[StopEventTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopEventType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_previous_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePreviousCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_onward_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOnwardCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_operating_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    use_realtime_data: Optional[UseRealtimeDataEnumeration] = field(
        default=None,
        metadata={
            "name": "UseRealtimeData",
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
    include_situations_context: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituationsContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_stop_hierarchy: Optional[HierarchyEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludeStopHierarchy",
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
