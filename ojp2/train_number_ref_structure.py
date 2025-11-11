from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainNumberRefStructure:
    """
    Type for reference to a TRAIN NUMBER.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
