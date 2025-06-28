from dataclasses import dataclass, field

from ojp2.vehicle_modes_of_transport_enumeration import (
    VehicleModesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMode:
    """
    Vehicle mode or mode of transport.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: VehicleModesOfTransportEnumeration = field(
        default=VehicleModesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
