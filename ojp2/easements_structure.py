from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.ticket_restriction_enumeration import TicketRestrictionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EasementsStructure:
    """
    Type for easement info.

    :ivar ticket_restrictions: Ticket restriction conditiosn in effect.
        TPEG pti table pti25.
    :ivar easement: Description of fare exceptions allowed because of
        disruption.  (Unbounded since SIRI 2.0)
    :ivar easement_ref: Refernce to a fare exceptions code that is
        allowed because of the disruption. An easement may relax a fare
        condition, for exampel "You may use your metro ticket on the
        bus', or 'You may use your bus ticket in teh metro between these
        two stops'.
    """

    ticket_restrictions: Optional[TicketRestrictionEnumeration] = field(
        default=None,
        metadata={
            "name": "TicketRestrictions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EasementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
