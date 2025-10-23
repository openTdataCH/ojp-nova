from dataclasses import dataclass, field
from ojp.refreshment_facility_enumeration import RefreshmentFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RefreshmentFacility:
    """Classification of Refreshment Facility type - Tpeg pti23."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RefreshmentFacilityEnumeration = field(
        default=RefreshmentFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
