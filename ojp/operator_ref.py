from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorRef:
    """
    Reference to an Operator ([TMv6] company  providing public transport
    services.)
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
