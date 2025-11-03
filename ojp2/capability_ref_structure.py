from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityRefStructure:
    """
    Type for capability ref.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
