from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_details_profile_enumeration import AccessibilityDetailsProfileEnumeration
from ojp.fare_param_structure import FareParamStructure
from ojp.operator_filter_structure import OperatorFilterStructure
from ojp.trip_content_filter_group_cycling_profile import TripContentFilterGroupCyclingProfile
from ojp.trip_content_filter_group_hiking_profile import TripContentFilterGroupHikingProfile
from ojp.use_realtime_data_enumeration import UseRealtimeDataEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripRefineParamStructure:
    """
    Trip refinement request parameter structure.

    :ivar foreign_object_refs: If true, then the request may contain
        object references from another system. Default is FALSE.
    :ivar refine_leg_ref: Refers to the legs to be refined by the
        server. If none is given, then all legs are open for refinement
        (depending if the relevant system can refine them).
    :ivar system_id: System reference to use for the refinement. If not
        specified the origin systems of each leg are used for the
        refinement.
    :ivar use_realtime_data: Usage of real-time data in refinement.
        Default is "full".
    :ivar operator_filter: Transport operators to include/exclude.
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
        and other accessibility-related information to retrieve (e.g.
        guidance text for the visually impaired).
    :ivar include_places_context: Whether the place context is needed.
        If a requestor has that information already, the response can be
        made slimmer, when set to false. Default is true.
    :ivar include_situations_context: Wheter the situation context is
        needed. If a requestor has that information by other means or
        can't process it, the response can be made slimmer, when set to
        false. Default is true
    :ivar include_intermediate_stops: Whether the result should include
        intermediate stops (between the passenger's board and alight
        stops).
    :ivar include_alternative_options: Whether alternative options
        should be presented as well. Mainly important for dominated
        journeys or in the case of ContinuousLegs the second-best route.
        Should be optimised for the user expectance (see. e.g
        https://theses.hal.science/tel-01848737). However, what the
        alternative options are may vary widely depending on the
        optimisation methods and filters.
    :ivar include_fare: Whether the result should include fare
        information.
    :ivar include_operating_days: Whether the result should include
        operating day information - as encoded bit string and in natural
        language.
    :ivar hiking_profile: Users hiking profile. The main element to
        control general walking behaviour is WalkSpeed (together with
        accessibility constraints). Note: possible explanations in
        German can be found here:
        https://akademie.alpinewelten.com/bergwandern/klassifizierung-
        von-wanderwegen
    :ivar cycling_profile: Cycling profile of the user (especially for
        sportive activities).
    :ivar trip_summary_only: If true, then the response will contain
        only summaries of the found trips. Default is false.
    :ivar fare_param: Parameters for fare calculation. Only used if
        IncludeFare is set (TripContentFilterGroup).
    :ivar extension:
    """
    foreign_object_refs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForeignObjectRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    refine_leg_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RefineLegRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    use_realtime_data: Optional[UseRealtimeDataEnumeration] = field(
        default=None,
        metadata={
            "name": "UseRealtimeData",
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
    include_access_features: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAccessFeatures",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_access_features_status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAccessFeaturesStatus",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_accessibility_details: List[AccessibilityDetailsProfileEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "IncludeAccessibilityDetails",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_places_context: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePlacesContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_situations_context: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituationsContext",
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
    include_alternative_options: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeAlternativeOptions",
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
    hiking_profile: Optional[TripContentFilterGroupHikingProfile] = field(
        default=None,
        metadata={
            "name": "HikingProfile",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    cycling_profile: Optional[TripContentFilterGroupCyclingProfile] = field(
        default=None,
        metadata={
            "name": "CyclingProfile",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_summary_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TripSummaryOnly",
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
