from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoringRefStructure:
    """
    Type for reference to a monitoring point (LOGICAL DISPLAY).
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
