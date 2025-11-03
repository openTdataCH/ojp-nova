from dataclasses import dataclass, field

from ojp2.key_value_structure import KeyValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class KeyListStructure:
    """Type for a Key List.

    (since SIRI 2.1)

    :ivar key_value: Key value pair for Entity.
    """

    key_value: list[KeyValueStructure] = field(
        default_factory=list,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
