from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EnvironmentReason:
    """DEPRECATED and changed to nmtoken since SIRI 2.1 (TPEG Pti22 - Environment Event Reason)"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
