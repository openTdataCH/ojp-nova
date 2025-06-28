from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PrivateCodeStructure:
    """
    Code within scope of a private referential system.

    :ivar system: Code of the foreign referential system.
    :ivar value: Object code within this private/foreign system.
    """

    system: Optional[str] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
