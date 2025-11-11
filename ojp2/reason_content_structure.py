from dataclasses import dataclass, field

from ojp2.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ReasonContentStructure:
    """
    :ivar reason_text: Reason of passenger information action in a
        specific language.
    """

    reason_text: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
