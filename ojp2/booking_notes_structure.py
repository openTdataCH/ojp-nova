from dataclasses import dataclass, field

from ojp2.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingNotesStructure:
    """
    A structure for an ordered list of booking notes.

    :ivar booking_note: Note about booking the LINE.
    """

    booking_note: list[InternationalTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookingNote",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
