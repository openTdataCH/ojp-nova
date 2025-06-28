from dataclasses import dataclass

from ojp2.entrance_to_vehicle_ref_structure import (
    EntranceToVehicleRefStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EntranceToVehicleRef(EntranceToVehicleRefStructure):
    """Reference to an ENTRANCE TO VEHICLE.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
