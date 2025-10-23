from dataclasses import dataclass, field
from ojp.hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HireFacility:
    """
    Classification of Hire Facility.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
