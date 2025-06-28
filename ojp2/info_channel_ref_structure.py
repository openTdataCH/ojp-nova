from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InfoChannelRefStructure:
    """
    Type for reference to an Info Channel.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
