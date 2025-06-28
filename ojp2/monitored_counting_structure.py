from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from ojp2.counted_feature_unit_enumeration import CountedFeatureUnitEnumeration
from ojp2.counting_trend_enumeration import CountingTrendEnumeration
from ojp2.counting_type_enumeration import CountingTypeEnumeration
from ojp2.extensions_2 import Extensions2
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoredCountingStructure:
    """
    Monitored counted values.

    :ivar counting_type: Nature of what is counted.
    :ivar counted_feature_unit: Unit of type for what is being counted
    :ivar type_of_counted_feature: Open ended type or refined
        classification of what is counted (complement to the information
        coming from the facility type itself)
    :ivar count: Counted value
    :ivar percentage: Value as a percentage (0.0 to 100.0) of the
        maximum possible value
    :ivar trend: Trend of the count
    :ivar accuracy: Accuracy of the count, as a percentage (0.0 to
        100.0), the percentage being a + or - maximum deviation from the
        provided value
    :ivar description: Description of what is counted
    :ivar counted_items_id_list: List of the IDs of the counted items:
        usefull mainly for reservation and detailed information purposes
    :ivar extensions:
    """

    counting_type: Optional[CountingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CountingType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    counted_feature_unit: Optional[CountedFeatureUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "CountedFeatureUnit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    type_of_counted_feature: Optional[TypeOfValueStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfCountedFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("0"),
        },
    )
    trend: Optional[CountingTrendEnumeration] = field(
        default=None,
        metadata={
            "name": "Trend",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accuracy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Accuracy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("0"),
        },
    )
    description: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    counted_items_id_list: Optional[
        "MonitoredCountingStructure.CountedItemsIdList"
    ] = field(
        default=None,
        metadata={
            "name": "CountedItemsIdList",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class CountedItemsIdList:
        """
        :ivar item_id: IDs of a counted item
        """

        item_id: list[str] = field(
            default_factory=list,
            metadata={
                "name": "ItemId",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
