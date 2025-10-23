from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownReason:
    """
    TPEG Pti18_0/TPEG unknown event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
