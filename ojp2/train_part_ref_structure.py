from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainPartRefStructure:
    """
    Type for reference to a Train Part.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
