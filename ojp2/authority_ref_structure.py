from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AuthorityRefStructure:
    """
    Type for a reference to an AUTHORITY.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 2,
        },
    )
