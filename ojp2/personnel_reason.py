from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PersonnelReason:
    """DEPRECATED and changed to nmtoken since SIRI 2.1 (TPEG Pti20 - Personnel Event Reason)"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
