from dataclasses import dataclass

from ojp2.local_service_structure import LocalServiceStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LocalService(LocalServiceStructure):
    """
    LOCAL SERVICe.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
