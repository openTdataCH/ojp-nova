from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class NavigationPathRefStructure:
    """
    Type for reference to a NAVIGATION PATH.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
