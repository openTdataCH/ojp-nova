from dataclasses import dataclass, field

from ojp2.category_key_value_type import CategoryKeyValueType

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestAdditionalInformationStructure:
    """
    Generic structure for additional information on POIs.

    :ivar poiadditional_information: POI additional information is a set
        of key/value pairs that are associated with defined categories.
    """

    poiadditional_information: list[CategoryKeyValueType] = field(
        default_factory=list,
        metadata={
            "name": "POIAdditionalInformation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
