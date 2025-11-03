from dataclasses import dataclass, field
from typing import Optional

from ojp2.dated_vehicle_journey_indirect_ref_structure import (
    DatedVehicleJourneyIndirectRefStructure,
)
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.line_ref_structure import LineRefStructure
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConnectingJourneyRefStructure:
    """
    Type for a reference to a connecting journey.

    :ivar framed_vehicle_journey_ref: A reference to the DATE VEHICLE
        JOURNEY that the VEHICLE is making, unique with the data horizon
        of the service.
    :ivar dated_vehicle_journey_indirect_ref: Identify a VEHICLE JOURNEY
        indirectly by origin and destination as well as the scheduled
        times at these stops.
    :ivar line_ref: Reference to LINE of journey.
    :ivar train_number_ref: Reference to TRAIN NUMBER of journey.
    :ivar operator_ref: Reference to OPERATOR of journey.
    :ivar participant_ref: PARTICIPANT reference that identifies data
        producer of journey.
    """

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "FramedVehicleJourneyRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    dated_vehicle_journey_indirect_ref: Optional[
        DatedVehicleJourneyIndirectRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyIndirectRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_number_ref: Optional[TrainNumberRefStructure] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
