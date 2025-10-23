from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ViaRef:
    """
    Reference to a SCHEDULED STOP POINT that is a VIA point on the journey.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
