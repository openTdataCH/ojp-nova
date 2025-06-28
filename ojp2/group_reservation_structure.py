from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class GroupReservationStructure:
    """Used to specify that a travel group has booked a section of the vehicle for
    a part of the journey, and if so under what name.

    (since SIRI 2.1)

    :ivar name_of_group: Name for which the travel group has made the
        reservation.
    :ivar number_of_reserved_seats: Number of seats that the group has
        booked.
    """

    name_of_group: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "NameOfGroup",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    number_of_reserved_seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
