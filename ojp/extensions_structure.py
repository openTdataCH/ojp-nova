from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ExtensionsStructure:
    """Type for Extensions to schema.

    Wraps an 'any' tag to ensure decidability.

    :ivar any_element: Placeholder for user extensions.
    """
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
