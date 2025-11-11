from dataclasses import dataclass

from ojp2.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleRef(VehicleRefStructure):
    """
    Reference to a VEHICLE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
