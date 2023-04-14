from dataclasses import dataclass, field
from typing import List, Optional, Union
from ojp.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeOrNilReasonListType:
    """gml:CodeOrNilReasonListType provides for lists of terms.

    The values in an instance element shall all be valid according to
    the rules of the dictionary, classification scheme, or authority
    identified by the value of its codeSpace attribute. An instance
    element may also include embedded values from NilReasonType. It is
    intended to be used in situations where a term or classification is
    expected, but the value may be absent for some reason.
    """
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )
