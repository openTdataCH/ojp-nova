from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affected_section_structure import AffectedSectionStructure
from ojp.affected_stop_point_structure import AffectedStopPointStructure
from ojp.direction_structure import DirectionStructure
from ojp.extensions_1 import Extensions1
from ojp.link_projection_structure import LinkProjectionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedRouteStructure:
    """
    Type for information about the routes affected by a SITUATION.

    :ivar route_ref: Reference to a ROUTE affected by SITUATION.
    :ivar direction: DIRECTIONS affected by SITUATION.
    :ivar sections: Sections of ROUTE affected by SITUATION.
    :ivar stop_points: Stop Poins of the ROUTE. Can be either all or
        only affected by SITUATION.
    :ivar route_links: ROUTE LINKs affected by SITUATION.
    :ivar extensions:
    """
    route_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    direction: List[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    sections: Optional["AffectedRouteStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_points: Optional["AffectedRouteStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    route_links: Optional["AffectedRouteStructure.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "RouteLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Sections:
        """
        :ivar affected_section: Sections of ROUTE that is affected by
            SITUATION.
        """
        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
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
            }
        )
        affected_stop_point: List[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
        link_projection_to_next_stop_point: List[LinkProjectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LinkProjectionToNextStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )

    @dataclass
    class RouteLinks:
        route_link_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "RouteLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
