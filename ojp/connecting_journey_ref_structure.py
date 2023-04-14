from dataclasses import dataclass, field
from typing import Optional
from ojp.framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConnectingJourneyRefStructure:
    """
    Type for a reference to a connecting journey.

    :ivar framed_vehicle_journey_ref: A reference to the DATE VEHICLE
        JOURNEY that the VEHICLE is making, unique with the data horizon
        of the service.
    :ivar line_ref: LINE Reference.
    :ivar participant_ref:
    """
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
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
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
