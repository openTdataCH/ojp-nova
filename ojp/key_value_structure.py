from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class KeyValueStructure:
    """Type for a Key List.

    (since SIRI 2.1)

    :ivar key: Identifier of value e.g. System.
    :ivar value: Value for alternative key.
    :ivar type_of_key: Identifier of type of key.
    """
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    type_of_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfKey",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
