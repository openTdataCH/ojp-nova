from dataclasses import dataclass

from ojp2.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleJourneyRef(VehicleJourneyRefStructure):
    """
    Reference to a VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
