from dataclasses import dataclass

from ojp2.compound_train_ref_structure import CompoundTrainRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CompoundTrainRef(CompoundTrainRefStructure):
    """Reference to a COMPOUND TRAIN.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
