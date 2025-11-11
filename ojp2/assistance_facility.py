from dataclasses import dataclass, field

from ojp2.assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AssistanceFacility:
    """
    Classification of Assistance Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AssistanceFacilityEnumeration = field(
        default=AssistanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
