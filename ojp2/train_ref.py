from dataclasses import dataclass

from ojp2.train_ref_structure import TrainRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainRef(TrainRefStructure):
    """Reference to a TRAIN.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
