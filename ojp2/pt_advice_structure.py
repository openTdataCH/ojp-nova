from dataclasses import dataclass, field
from typing import Optional

from ojp2.advice_ref_structure import AdviceRefStructure
from ojp2.advice_type_enumeration import AdviceTypeEnumeration
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtAdviceStructure:
    """Type for (structured) advice.

    The AdviceType enumerated value can be used to generate standardized messages describing the SITUATION. If no enumerated value is given, AdviceName is used instead.
    Note: this means that AdviceName is NOT a complete message, but only a (few) word(s) to be included in the message!
    Alternatively, AdviceRef can be used to reference a (complete) standardised advisory message.

    :ivar advice_ref: Reference to a standard advisory NOTICE to be
        given to passengers if a particular condition arises.
    :ivar advice_type: Structured classification of advice for
        passengers in the given SITUATION, from which a standardized
        message can be generated.
    :ivar advice_name: Textual classification of advice, from which a
        standardized message can be generated. Not normally needed,
        except when AdviceType is absent.
    :ivar details: Further textual advice to passengers.  (Unbounded
        since SIRI 2.0)
    """

    advice_ref: Optional[AdviceRefStructure] = field(
        default=None,
        metadata={
            "name": "AdviceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice_type: Optional[AdviceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AdviceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdviceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    details: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
