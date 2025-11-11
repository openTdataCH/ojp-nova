from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.accessibility_details_profile_enumeration import (
    AccessibilityDetailsProfileEnumeration,
)
from ojp2.fare_param_structure import FareParamStructure
from ojp2.line_direction_filter_structure import LineDirectionFilterStructure
from ojp2.mode_and_mode_of_operation_filter_structure import (
    ModeAndModeOfOperationFilterStructure,
)
from ojp2.multi_point_trip_param_structure_cycling_profile import (
    MultiPointTripParamStructureCyclingProfile,
)
from ojp2.multi_point_trip_param_structure_hiking_profile import (
    MultiPointTripParamStructureHikingProfile,
)
from ojp2.multi_point_type_enumeration import MultiPointTypeEnumeration
from ojp2.operator_filter_structure import OperatorFilterStructure
from ojp2.optimisation_method_enumeration import OptimisationMethodEnumeration
from ojp2.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp2.tariffzone_filter_structure import TariffzoneFilterStructure
from ojp2.use_realtime_data_enumeration import UseRealtimeDataEnumeration
from ojp2.vehicle_filter_structure import VehicleFilterStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiPointTripParamStructure:
    """
    Multi-point trip request parameter structure.

    :ivar mode_and_mode_of_operation_filter: MODEs and MODEs OF
        OPERATION to be considered in trip calculation. If only MODE is
        used, then it is for all MODE OF OPERATION. If combinations of
        MODE and MODE OF OPERATION are used (multiples), then all
        combinations are to be considered.
    :ivar line_filter: Lines/Directions to include/exclude.
    :ivar operator_filter: Transport operators to include/exclude.
    :ivar vehicle_filter: Filter for VEHICLE and TRAIN NUMBERs.
    :ivar tariffzone_filter: Filter for trips using only specific tariff
        zones.
    :ivar no_single_step: The user is not able to pass over (or wants to
        avoid) single steps. Stairs and non-level entrances are not
        excluded.
    :ivar no_stairs: The user is not able to walk up/downstairs.
    :ivar no_escalator: The user is not able to use an escalator.
    :ivar no_elevator: The user is not able to use an elevator.
    :ivar no_ramp: The user is not able to use a ramp.
    :ivar no_sight: The user is not able to see.
    :ivar no_travelator: The user is not able to use a travelator.
    :ivar level_entrance: The user needs vehicles with level entrance
        between platform and vehicle.
    :ivar level_entrance_or_boarding_aid: The user needs vehicles with
        level entrance between platform and vehicle, an appropriate
        ramp, or assistance for boarding or alighting (for assisted and
        unassisted wheelchairs, or similar constraints).
    :ivar bike_transport: The user wants to carry a bike on public
        transport (could be extended in future to transporting big
        luggage / animals / etc.).
    :ivar walk_speed: Deviation from average walking speed in percent.
        100% percent is average speed. Less than 100 % slower, Greater
        than 150% faster.
    :ivar additional_transfer_time: Additional time added to all
        transfers (also to transfers between individual to public
        transport, not modelled in Transmodel).
    :ivar hiking_profile: Users hiking profile. The main element to
        control general walking behaviour is WalkSpeed (together with
        accessibility constraints). Note: explanations in German can be
        found here:
        https://akademie.alpinewelten.com/bergwandern/klassifizierung-
        von-wanderwegen
    :ivar cycling_profile: Cycling profile of the user (especially for
        sportive activities).
    :ivar number_of_results: The number of trip results that the user
        wants to see at least. Be aware that some implementations will
        deliver one of the TripResults before the indicated departure
        time. This means that you can't assume that you get the exact
        number of results that you asked for in the request from the
        server.
    :ivar number_of_results_before: The desired number of trip results
        before the given time (at origin or destination).
    :ivar number_of_results_after: The desired number of trip results
        after the given time (at origin or destination).
    :ivar time_window: Time window in which the trips should be,
        starting from the time specified in PlaceContext. Implements
        TRIP REQUEST.FlexibilityWindow. All trips within the window
        should be provided by the implementation.
    :ivar use_realtime_data: The way real-time data should be used in
        the calculation of the trip.
    :ivar immediate_trip_start: Whether the trip calculation should find
        a solution that starts immediately (e.g., because the user is
        already on the way) instead of finding the latest possible start
        opportunity. Default is FALSE.
    :ivar transfer_limit: The maximum number of interchanges the user
        will accept per trip.
    :ivar optimisation_method: The type of algorithm to be used in the
        calculation of the trip (fastest, least walking, etc.).
    :ivar consider_elevation_data: Whether the trip calculation should
        take elevation data into account (bike, foot). Default is FALSE.
    :ivar include_all_restricted_lines: There might exist lines that
        have special restrictions and are not generally available to the
        public. E.g. school buses, company shuttles. dragLifts need to
        have an ACCESS MODE ski. Lines with ACCESS MODE bicycle will be
        included as well. If this flag is set, then existing restricted
        lines are considered by the router, irrespective of the selected
        passenger categories or the MotorisedMainTravelMode. The results
        are marked as restricted in the ServiceGroup. The usage could
        also be detailed with Attribute elements. Restricted trumps
        PassengerCategory, for example. If Restricted is set to true,
        all services are displayed.
    :ivar passenger_category: Sequence of all passenger categories, for
        which this search shall be conducted. In rare cases additional
        offerings may be available (e.g., demand responsive service with
        certain areas being reserved for seniors). If multiple
        PassengerCategories are provided, then Services are shown when
        they are available for at least one PassengerCategory.
    :ivar multi_point_type: Defines how the router should handle
        requests with multiple origins and destinations. As it is
        important for the strategy of the distributed trip planning the
        MultiPointType should be set. If the type is not supported a
        TRIP_MULTIPOINT_TYPE_NOT_SUPPORTED warning or error must be
        returned. Default is anyPoint.
    :ivar include_track_sections: Whether the result should include
        TrackSection elements to describe the geographic route of each
        journey leg.
    :ivar include_leg_projection: Whether the result should include the
        geographic projection (coordinates) of each journey leg.
    :ivar include_turn_description: Whether the result should include
        turn-by-turn instructions for each journey leg.
    :ivar include_access_features: Whether the result should include the
        access features (stairs, elevator, etc.) on each path link.
    :ivar include_access_features_status: Whether the result should
        include real time status of access features to indicate broken
        equipment.
    :ivar include_accessibility_details: Which accessibility features
        and other accessibility-related information to retrieve (e.g.,
        guidance text for the visually impaired).
    :ivar include_places_context: Whether the place context is needed.
        If a requestor has that information already, the response can be
        made slimmer, when set to false. Default is true.
    :ivar include_situations_context: Whether the situation context is
        needed. If a requestor has that information by other means or
        can't process it, the response can be made slimmer, when set to
        false. Default is true.
    :ivar include_intermediate_stops: Whether the result should include
        intermediate stops (between the passenger's board and alight
        stops).
    :ivar include_fare: Whether the result should include fare
        information.
    :ivar include_operating_days: Whether the result should include
        operating day information - as encoded bit string and in natural
        language.
    :ivar trip_summary_only: If true, then the response will contain
        only summaries of the found trips. Default is false.
    :ivar fare_param: Parameters for fare calculation. Only used if
        IncludeFare is set (TripContentFilterGroup).
    :ivar extension:
    """

    mode_and_mode_of_operation_filter: list[
        ModeAndModeOfOperationFilterStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "ModeAndModeOfOperationFilter",
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
    vehicle_filter: Optional[VehicleFilterStructure] = field(
        default=None,
        metadata={
            "name": "VehicleFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    tariffzone_filter: Optional[TariffzoneFilterStructure] = field(
        default=None,
        metadata={
            "name": "TariffzoneFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_single_step: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSingleStep",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_stairs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoStairs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_escalator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoEscalator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_elevator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoElevator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoRamp",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_sight: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_travelator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoTravelator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    level_entrance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LevelEntrance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    level_entrance_or_boarding_aid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LevelEntranceOrBoardingAid",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    bike_transport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BikeTransport",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    walk_speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "WalkSpeed",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    additional_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AdditionalTransferTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    hiking_profile: Optional[MultiPointTripParamStructureHikingProfile] = (
        field(
            default=None,
            metadata={
                "name": "HikingProfile",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    cycling_profile: Optional[MultiPointTripParamStructureCyclingProfile] = (
        field(
            default=None,
            metadata={
                "name": "CyclingProfile",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    number_of_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResults",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    number_of_results_before: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResultsBefore",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    number_of_results_after: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResultsAfter",
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
    use_realtime_data: Optional[UseRealtimeDataEnumeration] = field(
        default=None,
        metadata={
            "name": "UseRealtimeData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    immediate_trip_start: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ImmediateTripStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    transfer_limit: Optional[int] = field(
        default=None,
        metadata={
            "name": "TransferLimit",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    optimisation_method: Optional[OptimisationMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "OptimisationMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    consider_elevation_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConsiderElevationData",
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
    passenger_category: list[PassengerCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    multi_point_type: Optional[MultiPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MultiPointType",
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
    include_leg_projection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeLegProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_turn_description: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTurnDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_access_features: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAccessFeatures",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_access_features_status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAccessFeaturesStatus",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_accessibility_details: list[
        AccessibilityDetailsProfileEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "IncludeAccessibilityDetails",
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
    include_intermediate_stops: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeIntermediateStops",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeFare",
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
    trip_summary_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TripSummaryOnly",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_param: Optional[FareParamStructure] = field(
        default=None,
        metadata={
            "name": "FareParam",
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
