from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathLinkEndStructure:
    """
    Designations of a floor/level.

    :ivar level_public_code: Public identifier of the level as found on
        elevators and signs.
    :ivar level_name: Official name of the level.
    :ivar id: Id of the element at this end of the PathLink (typically a
        PLACE, e.g., where the elevator is located).
    """

    level_public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LevelPublicCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    level_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LevelName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
