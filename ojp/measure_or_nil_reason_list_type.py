from dataclasses import dataclass, field
from typing import List, Optional, Union
from ojp.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MeasureOrNilReasonListType:
    """gml:MeasureOrNilReasonListType provides for a list of quantities.

    An instance element may also include embedded values from
    NilReasonType. It is intended to be used in situations where a value
    is expected, but the value may be absent for some reason.
    """
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
