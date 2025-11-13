from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataFrameRefStructure:
    """
    Type for identifier of a data VERSION FRAME.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
