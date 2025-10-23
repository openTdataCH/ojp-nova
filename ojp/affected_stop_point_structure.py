from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_assessment_structure import AccessibilityAssessmentStructure
from ojp.affected_connection_link_structure import AffectedConnectionLinkStructure
from ojp.affected_modes_structure import AffectedModesStructure
from ojp.extensions_1 import Extensions1
from ojp.location_structure import LocationStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.route_point_type_enumeration import RoutePointTypeEnumeration
from ojp.stop_point_type_enumeration import StopPointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPointStructure:
    """
    Type for an SCHEDUELD STOP POINT affected by a SITUATION.

    :ivar stop_point_ref:
    :ivar private_ref: Alternative private code of stop.
    :ivar stop_point_name: Name of SCHEDULED STOP POIHT.  (Unbounded
        since SIRI 2.0)
    :ivar stop_point_type: Type of stop type. Normally implicit in
        VEHICLE mode. TPEG table pti 17_4
    :ivar location: Spatial coordinates of STOP POINT. Derivable from
        StopRef.
    :ivar affected_modes: Modes within station/stop affected by the
        SITUATION. If not specified, assume all modes of that station.
    :ivar place_ref: Refernce to a SITE or TOPOGRAPHIC PLACE affected by
        the Locality of stop (In UK NPtg Locality Code). Derivable from
        StopRef.
    :ivar place_name: Name of locality in which stop is found. Derivable
        from LocalityRef.  (Unbounded since SIRI 2.0)
    :ivar accessibility_assessment: Assesment of current ACCESSIBILITY
        of the STOP POINT as affected by the SITUATION.
    :ivar stop_condition: Status of STOP
    :ivar connection_links: CONNECTION links from stop.
    :ivar extensions:
    """
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    private_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_point_type: Optional[StopPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_modes: Optional[AffectedModesStructure] = field(
        default=None,
        metadata={
            "name": "AffectedModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_condition: List[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "StopCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connection_links: Optional["AffectedStopPointStructure.ConnectionLinks"] = field(
        default=None,
        metadata={
            "name": "ConnectionLinks",
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
    class ConnectionLinks:
        """
        :ivar affected_connection_link: CONNECTION LINKs from stop that
            are affected by the SITUATION.
        """
        affected_connection_link: List[AffectedConnectionLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedConnectionLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
