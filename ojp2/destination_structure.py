from dataclasses import dataclass, field
from typing import Optional

from ojp2.destination_ref_structure import DestinationRefStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DestinationStructure:
    """
    Type for Information about a DESTINATION.

    :ivar destination_ref: Identifer of Destinatioin
    :ivar destination_name: Name of Destination
    """

    destination_ref: Optional[DestinationRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    destination_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
