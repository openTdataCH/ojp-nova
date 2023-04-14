from dataclasses import dataclass, field
from typing import Optional
from ojp.general_attribute_structure import GeneralAttributeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LegAttributeStructure(GeneralAttributeStructure):
    """
    Attributes that are not valid on the whole service, but only on section of
    a TRIP made on a single MODE without interchange between boarding and
    alighting (facilities available on a specified (part of a) Leg of a VEHICLE
    JOURNEY)

    :ivar from_stop_seq_number: The attribute is valid from the stop
        point with this sequence number within the leg. If missing it is
        valid from the beginning of the leg.
    :ivar to_stop_seq_number: The attribute is valid to the stop point
        (inclusively) with this sequence number within the leg. If
        missing it is valid to the end of the leg.
    """
    from_stop_seq_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FromStopSeqNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    to_stop_seq_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToStopSeqNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
