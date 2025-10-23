from dataclasses import dataclass, field
from ojp.fare_class_facility_enumeration import FareClassFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FareClassFacility:
    """Classification of FareClass Facility type - Tpeg pti23."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FareClassFacilityEnumeration = field(
        default=FareClassFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
