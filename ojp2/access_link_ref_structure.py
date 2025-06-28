from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AccessLinkRefStructure:
    """
    Type for reference to an ACCESS link.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
