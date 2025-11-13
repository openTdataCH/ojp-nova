from dataclasses import dataclass

from ojp2.dated_vehicle_journey_structure import DatedVehicleJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourney(DatedVehicleJourneyStructure):
    """
    A planned VEHICLE JOURNEY taking place on a particular date.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
