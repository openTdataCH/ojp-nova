from dataclasses import dataclass

from ojp2.train_element_ref_structure import TrainElementRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainElementRef(TrainElementRefStructure):
    """Reference to a TRAIN ELEMENT.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
