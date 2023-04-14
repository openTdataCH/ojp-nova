from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassageBetweenTrainsStructure:
    """Indicates whether passengers have access to adjacent TRAINs or TRAIN
    COMPONENTs within a COMPOUND TRAIN, i.e., whether passage between those
    wagons/coaches is possible.

    (since SIRI 2.1)
    """
    train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passage_is_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PassageIsPossible",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
