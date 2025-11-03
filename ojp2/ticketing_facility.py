from dataclasses import dataclass, field

from ojp2.ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TicketingFacility:
    """Classification of Ticketing Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
