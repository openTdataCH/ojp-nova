from dataclasses import dataclass
from ojp.zone_projection_structure import ZoneProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class ZoneProjection(ZoneProjectionStructure):
    """
    PROJECTION onto a geospatial zone.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
