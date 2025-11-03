from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EntryQualifierStructure:
    """
    Type for a referenceUnique identifier of a SITUATION within participant.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
