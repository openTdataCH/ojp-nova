from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NetworkRefStructure:
    """
    Type for reference to an OPERATOR.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
