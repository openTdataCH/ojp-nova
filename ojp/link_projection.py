from dataclasses import dataclass
from ojp.link_projection_structure import LinkProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LinkProjection(LinkProjectionStructure):
    """
    Projection as a geospatial polyline.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
