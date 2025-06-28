from dataclasses import dataclass

from ojp2.train_element_structure import TrainElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainElement(TrainElementStructure):
    """An elementary component of a TRAIN, e.g. wagon or locomotive.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
