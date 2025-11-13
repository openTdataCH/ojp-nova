from dataclasses import dataclass, field

from ojp2.nuisance_facility_enumeration import NuisanceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NuisanceFacility:
    """Classification of Nuisance Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: NuisanceFacilityEnumeration = field(
        default=NuisanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
