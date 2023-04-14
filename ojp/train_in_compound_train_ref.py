from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainInCompoundTrainRef:
    """Reference to a TRAIN IN COMPOUND TRAIN.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
