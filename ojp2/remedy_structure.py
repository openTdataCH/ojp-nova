from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.half_open_timestamp_input_range_structure import (
    HalfOpenTimestampInputRangeStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.remedy_type_enumeration import RemedyTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RemedyStructure:
    """
    Description of the remedy to the change of a facility status (mainly when it
    becomes partially or totally anavailable)

    :ivar remedy_type: Type of the remedy (repair/replacement/remove)
    :ivar description: Description of the set up remedy in natural
        language.  (Unbounded since SIRI 2.0)
    :ivar remedy_period: Validity period for the remedy
    :ivar extensions:
    """

    remedy_type: Optional[RemedyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RemedyType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    remedy_period: Optional[HalfOpenTimestampInputRangeStructure] = field(
        default=None,
        metadata={
            "name": "RemedyPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
