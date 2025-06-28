from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OwnerRefStructure:
    """
    Reference to an ORGANISATION with ownership as the RESPONSIBILITY ROLE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
