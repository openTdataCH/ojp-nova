from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affected_connection_link_structure import AffectedConnectionLinkStructure
from ojp.extensions_1 import Extensions1
from ojp.interchange_status_enumeration import InterchangeStatusEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedInterchangeStructure:
    """
    Information about a SERVICE JOURNEY INTERCHANGE at CONNECTION link from a
    given SCHEDULED STOP POINT.

    :ivar interchange_ref: Reference to a SERVICE JOURNEY INTERCHANGE
        affected by a SITUATION.
    :ivar interchange_stop_point_ref: Identifier of STOP POINT of a stop
        at which VEHICLE JOURNEY meets for interchange If blank, same
        stop as destination. Reference to a STOP POINT.
    :ivar interchange_stop_point_name: Name of other Connecting STOP
        POINT of a connection. Derivable from InterchangeStopRef.
        (Unbounded since SIRI 2.0)
    :ivar connecting_vehicle_journey_ref: Reference to connecting
        VEHICLE JOURNEY affected by a SITUATION.
    :ivar interchange_status_type:
    :ivar connection_link: Reference to a CONNECTION Link affected by a
        SITUATION.
    :ivar extensions:
    """
    interchange_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    interchange_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    interchange_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connecting_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    interchange_status_type: Optional[InterchangeStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "InterchangeStatusType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    connection_link: List[AffectedConnectionLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLink",
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
