from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VersionRefStructure:
    """
    Type for reference Timetable Version.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
