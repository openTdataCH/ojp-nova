from dataclasses import dataclass
from ojp.train_structure import TrainStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Train(TrainStructure):
    """A vehicle composed of TRAIN ELEMENTs assembled in a certain order (so
    called TRAIN COMPONENTs), i.e. wagons assembled together and propelled by a
    locomotive or one of the wagons.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
