from dataclasses import dataclass

from ojp2.train_in_compound_train_structure import (
    TrainInCompoundTrainStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainInCompoundTrain(TrainInCompoundTrainStructure):
    """Specifies the order of a certain TRAIN within a COMPOUND TRAIN and how the
    TRAIN is labeled in that context.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
