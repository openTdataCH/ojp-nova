from dataclasses import dataclass, field
from ojp.luggage_facility_enumeration import LuggageFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LuggageFacility:
    """Classification of Luggage Facility type - Tpeg pti23."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: LuggageFacilityEnumeration = field(
        default=LuggageFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
