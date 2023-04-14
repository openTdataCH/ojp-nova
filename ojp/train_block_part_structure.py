from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainBlockPartStructure:
    """
    Type for BLOCK part elements of VEHICLE JOURNEY.

    :ivar number_of_block_parts: Total number of BLOCK parts making up
        the train of which this is part.
    :ivar train_part_ref: Reference to a train BLOCK part.
    :ivar position_of_train_block_part: Description of position of Train
        BLOCK Part within Train to guide passengers where to find it.
        E.g. 'Front four coaches'.
    """
    number_of_block_parts: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfBlockParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_part_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    position_of_train_block_part: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PositionOfTrainBlockPart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
