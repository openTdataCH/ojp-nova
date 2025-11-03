from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorDescriptionStructure:
    """
    Type for Description of an error.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
