from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationSimpleRefStructure:
    """Type for reference to a SITUATION.

    Includes the Particpant identifier and version components of the
    identifier.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
