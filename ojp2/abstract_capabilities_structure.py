from dataclasses import dataclass, field
from typing import Optional

from ojp2.capability_general_interaction_structure import (
    CapabilityGeneralInteractionStructure,
)
from ojp2.transport_description_structure import TransportDescriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractCapabilitiesStructure:
    """
    Type for Capabilities of StopMonitopring Service.

    :ivar general_interaction: General capabilities common to all SIRI
        service request types.
    :ivar transport_description: Implementation properties common to all
        request types.
    """

    general_interaction: Optional[CapabilityGeneralInteractionStructure] = (
        field(
            default=None,
            metadata={
                "name": "GeneralInteraction",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    transport_description: Optional[TransportDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "TransportDescription",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
