from dataclasses import dataclass, field
from typing import Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class InternationalTextStructure:
    """
    [a restricted view of ALTERNATIVE NAME in TMv6] alternative identified text
    to be used in specified languages.

    :ivar text: Text content.
    :ivar text_id: Id of this text. May be used for matching to pre-
        recorded audio files.
    """
    text: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    text_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
