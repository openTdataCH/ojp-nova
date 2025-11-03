from dataclasses import dataclass, field

from ojp2.passenger_information_facility_enumeration import (
    PassengerInformationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassengerInformationFacility:
    """Classification of PassengerInfo Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerInformationFacilityEnumeration = field(
        default=PassengerInformationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
