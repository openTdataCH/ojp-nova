from dataclasses import dataclass
from ojp.compound_train_structure import CompoundTrainStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CompoundTrain(CompoundTrainStructure):
    """Groups of carriages may be managed as sections by composing TRAINs into
    a COMPOUND TRAIN, for example if a TRAIN joins (or splits from) another
    TRAIN.

    (since SIRI 2.1) TRAINs within a COMPOUND TRAIN may have different
    origins and destinations due to joining/splitting. A COMPOUND TRAIN
    may be stable for one or multiple JOURNEY PARTs and change at a
    certain STOP POINT due to planned joining/splitting, despatching
    alterations or a situation.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
