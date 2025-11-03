from dataclasses import dataclass, field

from ojp2.osm_tag_structure import OsmTagStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestCategoryStructure:
    """
    [a view of POINT OF INTEREST CLASSIFICATION in TMv6] categorisation of POINTs
    OF INTEREST in respect of the activities undertaken at them (defined by key-
    value-pairs).

    :ivar osm_tag: OpenStreetMap tag structure (key-value)
    :ivar point_of_interest_classification: Classification of the POI
        (when it is not from OSM). The codification of the
        classification id may include de codification source (for
        example "IGN:[classificationCode]")
    """

    osm_tag: list[OsmTagStructure] = field(
        default_factory=list,
        metadata={
            "name": "OsmTag",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    point_of_interest_classification: list[str] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
