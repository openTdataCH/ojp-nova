from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedJourneyPartInfoStructure:
    """Type for a reference to JOURNEY PART.

    (since SIRI 2.1)

    :ivar journey_part_ref: Reference to a JOURNEY part.
    :ivar train_number_ref: Train Number for JOURNEY PART.
    :ivar operator_ref: OPERATOR of JOURNEY PART.
    :ivar compound_train_ref: Reference to COMPOUND TRAIN that
        represents the train formation/composition as a whole (for this
        JOURNEY PART). (since SIRI 2.1) A journey does always have one
        or more JOURNEY PARTs for which the train formation/composition
        remains unchanged.
    :ivar from_stop_point_ref: Reference to the SCHEDULED STOP POINT at
        which the related JOURNEY PART begins.
    :ivar to_stop_point_ref: Reference to the SCHEDULED STOP POINT at
        which the related JOURNEY PART ends.
    :ivar start_time: Time at which the related JOURNEY PART begins.
    :ivar end_time: Time at which the related JOURNEY PART ends.
    """
    journey_part_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    compound_train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    from_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    to_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
