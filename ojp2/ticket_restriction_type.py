from dataclasses import dataclass, field

from ojp2.ticket_restriction_enumeration import TicketRestrictionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TicketRestrictionType:
    """Ticket restrictions - TPEG Pti025"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketRestrictionEnumeration = field(
        default=TicketRestrictionEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
