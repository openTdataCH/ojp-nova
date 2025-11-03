from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class GroupOfLinesRefStructure:
    """
    Reference to a GROUP OF LINEs.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
