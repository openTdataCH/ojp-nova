from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministratorRefStructure:
    """
    Type for a reference to an ORGANISATION with administrative responsibility.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
