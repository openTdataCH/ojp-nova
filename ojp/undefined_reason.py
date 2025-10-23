from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UndefinedReason:
    """
    TPEG Pti18_255/TPEG Pti_22 undefined event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
