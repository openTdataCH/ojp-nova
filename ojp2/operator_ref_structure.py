from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OperatorRefStructure:
    """
    Reference to an OPERATOR.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
