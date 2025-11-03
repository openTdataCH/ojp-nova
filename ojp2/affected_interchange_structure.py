from dataclasses import dataclass, field
from typing import Optional

from ojp2.affected_connection_link_structure import (
    AffectedConnectionLinkStructure,
)
from ojp2.dated_vehicle_journey_ref_structure import (
    DatedVehicleJourneyRefStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.interchange_ref_structure import InterchangeRefStructure
from ojp2.interchange_status_type import InterchangeStatusType
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedInterchangeStructure:
    """
    Information about a SERVICE JOURNEY INTERCHANGE at CONNECTION link from a given
    SCHEDULED STOP POINT.

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

    interchange_ref: Optional[InterchangeRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_vehicle_journey_ref: Optional[
        DatedVehicleJourneyRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "ConnectingVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_status_type: Optional[InterchangeStatusType] = field(
        default=None,
        metadata={
            "name": "InterchangeStatusType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link: list[AffectedConnectionLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLink",
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
