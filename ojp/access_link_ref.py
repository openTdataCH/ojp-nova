from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AccessLinkRef:
    """
    Reference to an ACCESS link.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
