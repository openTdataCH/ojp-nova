from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityRefStructure:
    """
    Type for reference to a Faclility.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
