from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InfoLink:
    """
    Info Link .
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
