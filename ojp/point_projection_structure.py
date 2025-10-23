from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from ojp.abstract_projection import AbstractProjection

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PointProjectionStructure(AbstractProjection):
    """Type for geospatial Position of a point.

    May be expressed in concrete WGS 84 Coordinates or any GML
    compatible point coordinates format.

    :ivar longitude: Longitude from Greenwich Meridian. -180° (East) to
        +180° (West).
    :ivar latitude: Latitude from equator. -90° (South) to +90° (North).
    :ivar altitude: Altitude.
    :ivar coordinates: Coordinates of points in a GML compatible format,
        as indicated by srsName attribute.
    :ivar precision: Precision for point measurement. In meters.
    :ivar id: Identifier of POINT.
    :ivar srs_name: identifier of data reference system for geocodes, if
        point is specified as GML compatible Coordinates. A GML value.
        If not specified taken from system configuration.
    """
    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        }
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        }
    )
    altitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        }
    )
    coordinates: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "tokens": True,
        }
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
