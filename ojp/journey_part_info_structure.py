from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPartInfoStructure:
    """Type for a refernces to  JOURNEY PARTs.

    +SIRI v2.0

    :ivar journey_part_ref: Refrence to a JOURNEY part. +SIRI v2.0
    :ivar train_number_ref: Train Number for JOURNEY PART +SIRI v2.0
    :ivar operator_ref: Operator of JOURNEY PART. +SIRI v2.0
    """
    journey_part_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_number_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
