from dataclasses import dataclass
from ojp.abstract_ring_property_type import AbstractRingPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Interior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    The "interior" rings separate the surface / surface patch from the
    area enclosed by the rings.
    """
    class Meta:
        name = "interior"
        namespace = "http://www.opengis.net/gml/3.2"
