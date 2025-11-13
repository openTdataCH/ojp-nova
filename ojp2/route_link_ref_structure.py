from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RouteLinkRefStructure:
    """
    Reference to a ROUTE LINk.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
