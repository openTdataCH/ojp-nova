from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InfoLinkStructure1:
    """
    Type for Info Link.
    """

    class Meta:
        name = "InfoLinkStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
