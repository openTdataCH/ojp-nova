from dataclasses import dataclass, field

from ojp2.passenger_comms_facility_enumeration import (
    PassengerCommsFacilityEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassengerCommsFacility:
    """Classification of PassengerComms Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerCommsFacilityEnumeration = field(
        default=PassengerCommsFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
