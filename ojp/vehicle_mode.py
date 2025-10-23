from dataclasses import dataclass, field
from ojp.vehicle_modes_of_transport_enumeration import VehicleModesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMode:
    """
    Vehicle mode- Tpeg ModeType pti1.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: VehicleModesOfTransportEnumeration = field(
        default=VehicleModesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
