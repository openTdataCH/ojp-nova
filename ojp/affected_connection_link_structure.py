from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affected_path_link_structure import AffectedPathLinkStructure
from ojp.connection_direction_enumeration import ConnectionDirectionEnumeration
from ojp.empty_type import EmptyType
from ojp.extensions_1 import Extensions1
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.published_line_name import PublishedLineName

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedConnectionLinkStructure:
    """
    Type for a reference Information about a CONNECTION link from a given stop that
    is affected by a SITUATION.

    :ivar connection_link_ref: Reference to a CONNECTION link affected
        by a  SITUATION.
    :ivar connection_name: Name of CONNECTION link affected by a
        SITUATION.
    :ivar all_lines:
    :ivar line_ref:
    :ivar published_line_name:
    :ivar connecting_stop_point_ref: Reference to  other connecting STOP
        POINT of a CONNECTION link. If blank, both feeder and
        distributor vehicles go to same stop. Reference to a STOP POINT.
    :ivar connecting_stop_point_name: Name of other connecting STOP
        POINT of a CONNECTION link. Derivable from StopRef.  (Unbounded
        since SIRI 2.0)
    :ivar connecting_zone_ref: Zone in which connecting stop lies.
    :ivar connection_direction: Direction of SERVICE JOURNEY
        INTERCHANGE. Default is 'both'.
    :ivar affected_path_link: PATH LINKs affected by a SITUATION.
    :ivar extensions:
    """
    connection_link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connection_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    all_lines: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllLines",
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
    connecting_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connecting_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connecting_zone_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingZoneRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connection_direction: Optional[ConnectionDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_path_link: List[AffectedPathLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedPathLink",
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
