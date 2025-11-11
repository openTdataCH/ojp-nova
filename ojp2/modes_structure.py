from dataclasses import dataclass, field

from ojp2.all_modes_enumeration import AllModesEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ModesStructure:
    """
    Type for Transport MODEs.

    :ivar mode: A method of transportation such as bus, rail, etc.
    :ivar exclude: if true, listed modes to be excluded from list.
    """

    mode: list[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    exclude: bool = field(
        default=False,
        metadata={
            "name": "Exclude",
            "type": "Attribute",
        },
    )
