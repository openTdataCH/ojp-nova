from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affected_operator_structure import AffectedOperatorStructure
from ojp.affected_route_structure import AffectedRouteStructure
from ojp.affected_section_structure import AffectedSectionStructure
from ojp.affected_stop_point_structure import AffectedStopPointStructure
from ojp.direction_structure import DirectionStructure
from ojp.extensions_1 import Extensions1
from ojp.published_line_name import PublishedLineName

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedLineStructure:
    """
    Type for information about the LINEs affected by a SITUATION.

    :ivar affected_operator: Operators of LINEs affected by incident.
        Overrides any value specified for (i) Affected Network (ii)
        General Context.
    :ivar line_ref:
    :ivar published_line_name:
    :ivar destinations: DESTINATIONs to which the  LINE runs.
    :ivar direction: DIRECTIONs affected.
    :ivar routes: ROUTEs affected if  LINE has multiple ROUTEs.
    :ivar sections: Sections of  LINE affected.
    :ivar extensions:
    """
    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    published_line_name: Optional[PublishedLineName] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
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
    routes: Optional["AffectedLineStructure.Routes"] = field(
        default=None,
        metadata={
            "name": "Routes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    sections: Optional["AffectedLineStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
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
    class Routes:
        """
        :ivar affected_route: Route affected by Situation.
        """
        affected_route: List[AffectedRouteStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedRoute",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Sections:
        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
