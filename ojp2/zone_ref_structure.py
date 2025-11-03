from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ZoneRefStructure:
    """
    Type for a reference to a ZONE or locality.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
