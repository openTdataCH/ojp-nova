from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.line_direction_filter_structure import LineDirectionFilterStructure
from ojp.operator_filter_structure import OperatorFilterStructure
from ojp.pt_mode_filter_structure import PtModeFilterStructure
from ojp.stop_event_type_enumeration import StopEventTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventParamStructure:
    """
    Request specific parameters (parameters which define what is to be included in
    a Stop  Event result)

    :ivar pt_mode_filter: Modes to be considered in stop events.
    :ivar line_filter: Lines/Directions to include/exclude.
    :ivar operator_filter: Transport operators to include/exclude.
    :ivar number_of_results: parameter to control the number of TRIP
        results before/after a point in time. May NOT be used when
        departure time at origin AND arrival time at destination are set
    :ivar time_window: Time window events should lie within. Starting
        from time  given in LocationContext.
    :ivar stop_event_type: Only departures or arrivals or both.
    :ivar include_previous_calls: Whether the previous calls of each
        vehicle journey should be included in the response.
    :ivar include_onward_calls: Whether the onward calls of each vehicle
        journey should be included in the response.
    :ivar include_operating_days: Whether operating day information of
        this stop event should be included in the response.
    :ivar include_realtime_data: Whether realtime information of this
        stop event should be included in the response.
    """
    pt_mode_filter: Optional[PtModeFilterStructure] = field(
        default=None,
        metadata={
            "name": "PtModeFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    line_filter: Optional[LineDirectionFilterStructure] = field(
        default=None,
        metadata={
            "name": "LineFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operator_filter: Optional[OperatorFilterStructure] = field(
        default=None,
        metadata={
            "name": "OperatorFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    number_of_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResults",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_window: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeWindow",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_event_type: Optional[StopEventTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopEventType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_previous_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePreviousCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_onward_calls: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOnwardCalls",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_operating_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_realtime_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeRealtimeData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
