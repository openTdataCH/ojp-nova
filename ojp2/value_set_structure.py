from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.values_structure import ValuesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ValueSetStructure:
    """Type for a VALUE SET.

    Used to define open classifications of value types. (since SIRI 2.1)

    :ivar value_set_code: Identifier of VALUE SET.
    :ivar class_of_values: Name of Class of values in set.
    :ivar name: Name of set.
    :ivar values: Values in set.
    """

    value_set_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueSetCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    class_of_values: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassOfValues",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    values: Optional[ValuesStructure] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
