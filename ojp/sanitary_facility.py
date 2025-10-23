from dataclasses import dataclass, field
from ojp.sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SanitaryFacility:
    """Classification of Sanitary Facility type - Tpeg pti23."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SanitaryFacilityEnumeration = field(
        default=SanitaryFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
