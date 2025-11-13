from dataclasses import dataclass, field

from ojp2.access_modes_enumeration import AccessModesEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AccessModesListOfEnumerations:
    """
    List of Access Modes.

    :ivar access_mode: Access mode that should be considered.
    """

    access_mode: list[AccessModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
