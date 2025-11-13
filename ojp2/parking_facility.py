from dataclasses import dataclass, field
from typing import Optional

from ojp2.parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParkingFacility:
    """
    Classification of Access Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[ParkingFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
