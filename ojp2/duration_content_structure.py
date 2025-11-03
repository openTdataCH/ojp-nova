from dataclasses import dataclass, field

from ojp2.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DurationContentStructure:
    """
    :ivar duration_text: Indicates the currently expected duration of a
        SITUATION in a specific language. An estimation should be given
        here, because an indefinite duration is not helpful to the
        passenger. The duration can be adjusted at any time, if the
        traffic operator has additional information.
    """

    duration_text: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "DurationText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
