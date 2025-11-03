from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class QuayRefStructure2:
    """
    Type for reference to a QUAY.
    """

    class Meta:
        name = "QuayRefStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
