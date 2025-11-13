from dataclasses import dataclass, field

from ojp2.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SummaryContentStructure:
    """
    :ivar summary_text: Summary of passenger information action in a
        specific language.
    """

    summary_text: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "SummaryText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
