from dataclasses import dataclass, field
from typing import Optional

from ojp2.connecting_journey_ref_structure import ConnectingJourneyRefStructure
from ojp2.related_call_structure import RelatedCallStructure
from ojp2.related_journey_part_structure import RelatedJourneyPartStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedJourneyStructure(ConnectingJourneyRefStructure):
    """
    :ivar call_info: Information about the stop at which the JOURNEY is
        related to another JOURNEY. (since SIRI 2.1)
    :ivar journey_parts: Information about the JOURNEY PARTs for which
        the JOURNEY has a JOURNEY RELATION. (since SIRI 2.1)
    """

    call_info: Optional[RelatedCallStructure] = field(
        default=None,
        metadata={
            "name": "CallInfo",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional["RelatedJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class JourneyParts:
        """
        :ivar journey_part_info: Information about related parts of
            JOURNEY. (since SIRI 2.1)
        """

        journey_part_info: list[RelatedJourneyPartStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
