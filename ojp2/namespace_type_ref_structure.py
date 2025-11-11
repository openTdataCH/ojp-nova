from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class NamespaceTypeRefStructure:
    """
    Type for a reference to an Namespace.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
