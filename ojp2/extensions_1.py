from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class Extensions1:
    """
    Arbitrary extensions.
    """

    class Meta:
        name = "Extensions"
        namespace = "http://www.ifopt.org.uk/ifopt"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
