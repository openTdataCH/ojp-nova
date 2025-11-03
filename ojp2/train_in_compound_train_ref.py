from dataclasses import dataclass

from ojp2.train_in_compound_train_ref_structure import (
    TrainInCompoundTrainRefStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainInCompoundTrainRef(TrainInCompoundTrainRefStructure):
    """Reference to a TRAIN IN COMPOUND TRAIN.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
