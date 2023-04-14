from dataclasses import dataclass, field
from typing import List, Optional
from ojp.fare_param_structure import FareParamStructure
from ojp.individual_modes_enumeration import IndividualModesEnumeration
from ojp.line_direction_filter_structure import LineDirectionFilterStructure
from ojp.operator_filter_structure import OperatorFilterStructure
from ojp.optimisation_method_enumeration import OptimisationMethodEnumeration
from ojp.private_mode_filter_structure import PrivateModeFilterStructure
from ojp.pt_mode_filter_structure import PtModeFilterStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripParamStructure:
    """
    Trip request parameter structure.

    :ivar pt_mode_filter: Modes to be considered in trip calculation.
    :ivar line_filter: Lines/Directions to include/exclude.
    :ivar operator_filter: Transport operators to include/exclude.
    :ivar private_mode_filter: Private mobility options to
        include/exclude.
    :ivar no_single_step: The user is not able to climb one step.
    :ivar no_stairs: The user is not able to walk up/down stairs.
    :ivar no_escalator: The user is not able to use an escalator.
    :ivar no_elevator: The user is not able to use an elevator.
    :ivar no_ramp: The user is not able to use an ramp.
    :ivar level_entrance: The user needs vehicles with level entrance
        between  platform and vehicle, f.e. for wheelchair access.
    :ivar bike_transport: The user wants to carry a bike on public
        transport.
    :ivar walk_speed: Deviation from average walk speed in percent. 100%
        percent is average speed. Less than 100 % slower, Greater than
        150% faster.
    :ivar number_of_results: The number of trip results that the user
        wants to see at least.
    :ivar number_of_results_before: The desired number of trip results
        before the given time (at origin or destination).
    :ivar number_of_results_after: The desired number of trip results
        after the given time (at origin or destination).
    :ivar ignore_realtime_data: The trip calculation should not use any
        realtime or incident data.
    :ivar immediate_trip_start: Whether the trip calculation should find
        a solution that starts immediately (f.e. because the user is
        already on the way) instead of finding the latest possible start
        opportunity.
    :ivar transfer_limit: The maximum number of interchanges the user
        will accept per trip.
    :ivar optimisation_method: the types of algorithm that can be used
        for planning a journey (fastest, least walking, etc)
    :ivar it_modes_to_cover: For each mode in this list a separate
        monomodal trip shall be found - in addition to inter-modal
        solutions.
    :ivar accept_deferred_delivery: If yes, then with the first response
        a summary of the trip solution(s) is enough. Full trip
        information is sent actively by the server to the Address stated
        in RequestorEndpointGroup. Default is false.
    :ivar include_track_sections: Whether the result should include
        TrackSection elements to describe the geographic route of each
        journey leg.
    :ivar include_leg_projection: Whether the result should include the
        geographic projection (coordinates) of each journey leg.
    :ivar include_turn_description: Whether the result should include
        turn-by-turn instructions for each journey leg.
    :ivar include_accessibility: Whether the result should include
        accessibility information.
    :ivar include_intermediate_stops: Whether the result should include
        intermediate stops (between the passenger's board and alight
        stops).
    :ivar include_fare: Whether the result should include fare
        information.
    :ivar include_operating_days: Whether the result should include
        operating day information - as encoded bit string and in natural
        language.
    :ivar fare_param:
    :ivar extension:
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
    private_mode_filter: Optional[PrivateModeFilterStructure] = field(
        default=None,
        metadata={
            "name": "PrivateModeFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_single_step: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSingleStep",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_stairs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoStairs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_escalator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoEscalator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_elevator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoElevator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoRamp",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    level_entrance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LevelEntrance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    bike_transport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BikeTransport",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    walk_speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "WalkSpeed",
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
    number_of_results_before: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResultsBefore",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    number_of_results_after: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResultsAfter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ignore_realtime_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IgnoreRealtimeData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    immediate_trip_start: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ImmediateTripStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    transfer_limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "TransferLimit",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    optimisation_method: Optional[OptimisationMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "OptimisationMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    it_modes_to_cover: List[IndividualModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ItModesToCover",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    accept_deferred_delivery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptDeferredDelivery",
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
    include_leg_projection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeLegProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_turn_description: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTurnDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_accessibility: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAccessibility",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_intermediate_stops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeIntermediateStops",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeFare",
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
    fare_param: Optional[FareParamStructure] = field(
        default=None,
        metadata={
            "name": "FareParam",
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
