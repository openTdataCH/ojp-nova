from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RouteRefStructure:
    """
    Reference to a Route (Transmodel)
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
