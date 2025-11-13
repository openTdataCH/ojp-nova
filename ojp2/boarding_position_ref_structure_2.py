from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BoardingPositionRefStructure2:
    """
    Type for reference to a BOARDING POSITION.
    """

    class Meta:
        name = "BoardingPositionRefStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
