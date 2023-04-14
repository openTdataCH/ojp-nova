from dataclasses import dataclass
from ojp.train_component_structure import TrainComponentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainComponent(TrainComponentStructure):
    """Specifies the order of a certain TRAIN ELEMENT within a TRAIN and how
    the TRAIN ELEMENT is labeled in that context.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
