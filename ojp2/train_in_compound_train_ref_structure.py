from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainInCompoundTrainRefStructure:
    """Type for reference to a TRAIN IN COMPOUND TRAIN.

    (since SIRI 2.1)
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
