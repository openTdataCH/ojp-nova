from dataclasses import dataclass, field

from ojp2.accommodation_facility_enumeration import (
    AccommodationFacilityEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AccommodationFacility:
    """Classification of Accomodation Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
