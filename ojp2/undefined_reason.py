from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UndefinedReason:
    """DEPRECATED since SIRI 2.1 (TPEG Pti18_255 - undefined event reason)."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
