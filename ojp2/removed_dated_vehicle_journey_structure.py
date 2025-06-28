from dataclasses import dataclass, field
from typing import Optional

from ojp2.dated_vehicle_journey_indirect_ref_structure import (
    DatedVehicleJourneyIndirectRefStructure,
)
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.reason_for_removal import ReasonForRemoval
from ojp2.train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RemovedDatedVehicleJourneyStructure:
    """Type for previously planned VEHICLE JOURNEY that is removed from the data
    producer when using incremental updates.

    (since SIRI 2.1)

    :ivar framed_vehicle_journey_ref: A reference to the DATED VEHICLE
        JOURNEY from a previous PT delivery that is removed by the data
        producer.
    :ivar dated_vehicle_journey_indirect_ref: Optionally identify the
        VEHICLE JOURNEY indirectly by origin and destination and the
        scheduled times at these stops.
    :ivar train_numbers: TRAIN NUMBERs for journey.
    :ivar reason_for_removal:
    """

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "FramedVehicleJourneyRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
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
    train_numbers: Optional[
        "RemovedDatedVehicleJourneyStructure.TrainNumbers"
    ] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_for_removal: Optional[ReasonForRemoval] = field(
        default=None,
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )

    @dataclass
    class TrainNumbers:
        """
        :ivar train_number_ref: TRAIN NUMBER assigned to VEHICLE
            JOURNEY.
        """

        train_number_ref: list[TrainNumberRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
