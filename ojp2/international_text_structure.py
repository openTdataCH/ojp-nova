from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class InternationalTextStructure:
    """
    [a restricted view of ALTERNATIVE NAME in TMv6] alternative identified text to
    be used in specified languages.

    :ivar text: Text content.
    :ivar text_id: Id of this text. May be used for matching to pre-
        recorded audio files.
    """

    text: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
    text_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
