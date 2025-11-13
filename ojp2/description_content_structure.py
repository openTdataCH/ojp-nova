from dataclasses import dataclass, field
from typing import Optional

from ojp2.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DescriptionContentStructure:
    """
    :ivar description_text: Description of passenger information action
        in a specific language. Should not repeat any strap line
        included in Summary.
    :ivar description_priority: Prioritises a description from the
        information owner's point of view, e.g. usable for sorting or
        hiding individual descriptions. 1 = highest priority.
    """

    description_text: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    description_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DescriptionPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
