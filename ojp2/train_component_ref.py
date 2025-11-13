from dataclasses import dataclass

from ojp2.train_component_ref_structure import TrainComponentRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainComponentRef(TrainComponentRefStructure):
    """Reference to a TRAIN COMPONENT.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
