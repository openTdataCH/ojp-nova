from dataclasses import dataclass
from ojp.passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ExpectedDepartureCapacities(PassengerCapacityStructure):
    """Expected/Predicted real-time capacities (number of available seats) of a
    VEHICLE after departing from a given stop.

    Alternative way to communicate occupancy measurements. (since SIRI
    2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
