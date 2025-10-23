from dataclasses import dataclass, field
from ojp.mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MobilityFacility:
    """Classification of Mobility Facility type - Tpeg pti23."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
