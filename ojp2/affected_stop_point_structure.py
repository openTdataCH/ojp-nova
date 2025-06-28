from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.affected_connection_link_structure import (
    AffectedConnectionLinkStructure,
)
from ojp2.affected_facility_structure import AffectedFacilityStructure
from ojp2.affected_modes_structure import AffectedModesStructure
from ojp2.affected_operator_structure import AffectedOperatorStructure
from ojp2.affected_section_structure import AffectedSectionStructure
from ojp2.affected_stop_place_component_structure import (
    AffectedStopPlaceComponentStructure,
)
from ojp2.affected_stop_place_element_structure import (
    AffectedStopPlaceElementStructure,
)
from ojp2.direction_structure import DirectionStructure
from ojp2.extensions_2 import Extensions2
from ojp2.line_ref import LineRef
from ojp2.link_projection_structure import LinkProjectionStructure
from ojp2.location_structure import LocationStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.navigation_path_ref_structure import NavigationPathRefStructure
from ojp2.published_line_name import PublishedLineName
from ojp2.route_link_ref_structure import RouteLinkRefStructure
from ojp2.route_point_type_enumeration import RoutePointTypeEnumeration
from ojp2.route_ref_structure import RouteRefStructure
from ojp2.stop_place_ref_structure_1 import StopPlaceRefStructure1
from ojp2.stop_place_type_enumeration import StopPlaceTypeEnumeration
from ojp2.stop_point_ref import StopPointRef
from ojp2.stop_point_type_enumeration import StopPointTypeEnumeration
from ojp2.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPointStructure:
    """
    Type for an SCHEDULED STOP POINT affected by a SITUATION.

    :ivar stop_point_ref:
    :ivar private_ref: Alternative private code of stop.
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar stop_point_type: Type of stop type. Normally implicit in
        VEHICLE mode. TPEG table pti 17_4
    :ivar location: Spatial coordinates of STOP POINT. Derivable from
        StopRef.
    :ivar stop_place_ref: Reference of STOP PLACE related to this
        affected StopPoint.
    :ivar stop_place_name: Name of STOP PLACE related to this affected
        StopPoint.  (Unbounded to allow a text for every language)
    :ivar affected_modes: Modes within station/stop affected by the
        SITUATION. If not specified, assume all modes of that station.
    :ivar place_ref: Reference to a SITE or TOPOGRAPHIC PLACE affected
        by the Locality of stop (In UK NPtg Locality Code). Derivable
        from StopRef.
    :ivar place_name: Name of locality in which stop is found. Derivable
        from LocalityRef.  (Unbounded since SIRI 2.0)
    :ivar accessibility_assessment: Assessment of current ACCESSIBILITY
        of the STOP POINT as affected by the SITUATION.
    :ivar stop_condition: Status of STOP
    :ivar connection_links: CONNECTION links from stop.
    :ivar lines: Used to restrict stop points to some lines
    :ivar extensions:
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_type: Optional[StopPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRefStructure1] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_modes: Optional[AffectedModesStructure] = field(
        default=None,
        metadata={
            "name": "AffectedModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = (
        field(
            default=None,
            metadata={
                "name": "AccessibilityAssessment",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    stop_condition: list[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StopCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_links: Optional[
        "AffectedStopPointStructure.ConnectionLinks"
    ] = field(
        default=None,
        metadata={
            "name": "ConnectionLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AffectedStopPointStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ConnectionLinks:
        """
        :ivar affected_connection_link: CONNECTION LINKs from stop that
            are affected by the SITUATION.
        """

        affected_connection_link: list[AffectedConnectionLinkStructure] = (
            field(
                default_factory=list,
                metadata={
                    "name": "AffectedConnectionLink",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                    "min_occurs": 1,
                },
            )
        )

    @dataclass
    class Lines:
        affected_line: list["AffectedLineStructure"] = field(
            default_factory=list,
            metadata={
                "name": "AffectedLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedRouteStructure:
    """An ordered list of MAPPING POINTs defining one single path through the road
    (or rail) Network.

    A ROUTE may pass through the same MAPPING POINT more than once.

    :ivar route_ref: Reference to a ROUTE affected by SITUATION.
    :ivar direction: DIRECTIONS affected by SITUATION.
    :ivar sections: Sections of ROUTE affected by SITUATION.
    :ivar stop_points: Stop Poins of the ROUTE. Can be either all or
        only affected by SITUATION.
    :ivar route_links: ROUTE LINKs affected by SITUATION.
    :ivar extensions:
    """

    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: list[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedRouteStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectedRouteStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_links: Optional["AffectedRouteStructure.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "RouteLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Sections:
        """
        :ivar affected_section: Sections of ROUTE that is affected by
            SITUATION.
        """

        affected_section: list[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPoints:
        """
        :ivar affected_only: Indicates whether the list of STOP POINTS
            contains all STOP POINTS of ROUTE or only affected by
            SITUATION.
        :ivar affected_stop_point: Stop Point of the ROUTE
        :ivar link_projection_to_next_stop_point: GIs projection of Link
            to the next provided StopPoint. NB Line here means Geometry
            Polyline, not Transmodel Transport Line.
        """

        affected_only: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AffectedOnly",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        affected_stop_point: list[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
        link_projection_to_next_stop_point: list[LinkProjectionStructure] = (
            field(
                default_factory=list,
                metadata={
                    "name": "LinkProjectionToNextStopPoint",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
        )

    @dataclass
    class RouteLinks:
        route_link_ref: list[RouteLinkRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "RouteLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedLineStructure:
    """Information about the individual LINEs in the network that are affected by a
    SITUATION.

    If not explicitly overridden, modes and submodes will be defaulted
    to any values present (i) in the AffectedNetwork (ii) in the general
    context.

    :ivar affected_operator: Restricts the affected scope to the
        specified operators of LINEs that are affected by the situation.
        Overrides any value specified for (i) Affected Network (ii)
        General Context.
    :ivar line_ref:
    :ivar published_line_name:
    :ivar origins: Restricts the affected scope to the specified origins
    :ivar destinations: Restricts the affected scope to the specified
        DESTINATIONs
    :ivar direction: DIRECTIONs affected.
    :ivar routes: Restricts the affected scope to the specified ROUTEs
    :ivar sections: Restricts the affected scope to the specified LINE
        SECTIONs
    :ivar stop_points: Restricts the affected scope to the specified
        SCHEDULED STOP POINTs
    :ivar stop_places: Restricts the affected scope to the specified
        STOP PLACEs
    :ivar extensions:
    """

    affected_operator: list[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    published_line_name: list[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origins: list[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: list[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: list[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes: Optional["AffectedLineStructure.Routes"] = field(
        default=None,
        metadata={
            "name": "Routes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedLineStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectedLineStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_places: Optional["AffectedLineStructure.StopPlaces"] = field(
        default=None,
        metadata={
            "name": "StopPlaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Routes:
        """
        :ivar affected_route: Route affected by Situation.
        """

        affected_route: list[AffectedRouteStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedRoute",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Sections:
        affected_section: list[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPoints:
        affected_stop_point: list[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPlaces:
        affected_stop_place: list["AffectedStopPlaceStructure"] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedStopPlaceStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the STOP PLACEs affected by an SITUATION.

    :ivar stop_place_ref: Identifier of STOP PLACE affected by
        SITUATION.
    :ivar place_name: Name of STOP PLACE.  (Unbounded since SIRI 2.0)
    :ivar stop_place_type: Type of STOP PLACE.
    :ivar affected_facilities: Facilities available for VEHICLE JOURNEY
        (since SIRI 2.0)
    :ivar affected_components: Quays affected by SITUATION.
    :ivar affected_navigation_paths: PathLinks affected by SITUATION.
    :ivar lines: Used to restrict STOP PLACEs to some lines
    :ivar extensions:
    """

    stop_place_ref: Optional[StopPlaceRefStructure1] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    place_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_type: Optional[StopPlaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_facilities: Optional[
        "AffectedStopPlaceStructure.AffectedFacilities"
    ] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_components: Optional[
        "AffectedStopPlaceStructure.AffectedComponents"
    ] = field(
        default=None,
        metadata={
            "name": "AffectedComponents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_navigation_paths: Optional[
        "AffectedStopPlaceStructure.AffectedNavigationPaths"
    ] = field(
        default=None,
        metadata={
            "name": "AffectedNavigationPaths",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AffectedStopPlaceStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class AffectedFacilities:
        """
        :ivar affected_facility: Facililitiy available for VEHICLE
            JOURNEY   (since SIRI 2.0)
        """

        affected_facility: list[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class AffectedComponents:
        """
        :ivar affected_component: Quay affected by SITUATION.
        """

        affected_component: list[AffectedStopPlaceComponentStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedComponent",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class AffectedNavigationPaths:
        navigation_path_ref: list[NavigationPathRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "NavigationPathRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Lines:
        affected_line: list[AffectedLineStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
