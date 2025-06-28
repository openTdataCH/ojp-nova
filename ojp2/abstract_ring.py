from dataclasses import dataclass

from ojp2.abstract_ring_type import AbstractRingType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractRing(AbstractRingType):
    """An abstraction of a ring to support surface boundaries of different
    complexity.

    The AbstractRing element is the abstract head of the substitution
    group for all closed boundaries of a surface patch.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
