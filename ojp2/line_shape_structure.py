from dataclasses import dataclass, field

from ojp2.location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineShapeStructure:
    """
    Defines a line shape (since SIRI 2.0)

    :ivar point: A geospatial point. (since SIRI 2.0)
    """

    point: list[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        },
    )
