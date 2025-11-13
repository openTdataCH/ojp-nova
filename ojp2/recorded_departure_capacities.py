from dataclasses import dataclass

from ojp2.passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RecordedDepartureCapacities(PassengerCapacityStructure):
    """Actually recorded/counted capacities of a VEHICLE after departing from a
    given stop.

    Alternative way to communicate occupancy measurements. (since SIRI
    2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
