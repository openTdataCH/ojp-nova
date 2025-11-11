from dataclasses import dataclass

from ojp2.dated_vehicle_journey_ref_structure import (
    DatedVehicleJourneyRefStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyRef(DatedVehicleJourneyRefStructure):
    """
    Reference to a DATED VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
