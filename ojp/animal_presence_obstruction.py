from dataclasses import dataclass, field
from typing import Optional
from ojp.animal_presence_type_enum import AnimalPresenceTypeEnum
from ojp.extension_type import ExtensionType
from ojp.obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AnimalPresenceObstruction(Obstruction):
    alive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    animal_presence_type: Optional[AnimalPresenceTypeEnum] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
