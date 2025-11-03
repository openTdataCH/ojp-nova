from dataclasses import dataclass, field
from typing import Optional

from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DirectionStructure:
    """
    Type for DIRECTION.

    :ivar direction_ref: Identifer of DIRECTION,
    :ivar direction_name: Description of DIRECTION.  (Unbounded since
        SIRI 2.0)
    """

    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    direction_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
