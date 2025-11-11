from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.train_element import TrainElement
from ojp2.train_element_ref import TrainElementRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainComponentStructure:
    """Type for TRAIN COMPONENT.

    (since SIRI 2.1)

    :ivar train_component_code: Identifier for TRAIN COMPONENT.
    :ivar order: Specifies the order of the TRAIN ELEMENT within the
        TRAIN. The locomotive would ideally have ORDER '1', the first
        wagon/coach attached to the locomotive ORDER '2' and so on.
    :ivar label: Specifies how the TRAIN ELEMENT is labeled within the
        context of the TRAIN. This advertised label or number, e.g.
        "Carriage B" or "23", can be used for seat reservations and
        passenger orientation.
    :ivar description: Description of TRAIN COMPONENT, e.g. "Front
        Carriage 1st Class".
    :ivar train_element_ref:
    :ivar train_element:
    :ivar reversed_orientation: Whether orientation of TRAIN ELEMENT
        within TRAIN is reversed or not. Default is 'false', i.e., they
        have the same orientation (usually forward in the direction of
        travel).
    """

    train_component_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainComponentCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    label: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_element: Optional[TrainElement] = field(
        default=None,
        metadata={
            "name": "TrainElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
