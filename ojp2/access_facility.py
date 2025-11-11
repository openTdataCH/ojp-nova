from dataclasses import dataclass, field

from ojp2.access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AccessFacility:
    """
    Classification of Access Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccessFacilityEnumeration = field(
        default=AccessFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
