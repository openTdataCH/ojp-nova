from dataclasses import dataclass, field
from typing import List, Optional
from ojp.multilingual_string_value import MultilingualStringValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MultilingualString:
    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
                "min_occurs": 1,
            }
        )
