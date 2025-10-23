from dataclasses import dataclass, field
from ojp.reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ReservedSpaceFacility:
    """
    Classification of Reserved Space Facility.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
