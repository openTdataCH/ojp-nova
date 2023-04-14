from dataclasses import dataclass
from ojp.vehicle_occupancy_structure import VehicleOccupancyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RecordedDepartureOccupancy(VehicleOccupancyStructure):
    """Actually recorded/counted occupancies of a VEHICLE and reserved seats
    after departing from a given stop.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
