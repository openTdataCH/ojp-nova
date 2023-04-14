from dataclasses import dataclass, field
from ojp.retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RetailFacility:
    """
    Classification of Retail Facility.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
