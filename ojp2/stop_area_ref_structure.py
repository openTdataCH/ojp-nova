from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopAreaRefStructure:
    """
    Reference to a  STOP AREA.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
