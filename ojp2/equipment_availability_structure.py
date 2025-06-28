from dataclasses import dataclass, field
from typing import Optional

from ojp2.equipment_ref_structure import EquipmentRefStructure
from ojp2.equipment_status_enumeration import EquipmentStatusEnumeration
from ojp2.equipment_type_ref_structure import EquipmentTypeRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.feature_ref_structure_2 import FeatureRefStructure2
from ojp2.half_open_timestamp_output_range_structure import (
    HalfOpenTimestampOutputRangeStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EquipmentAvailabilityStructure:
    """
    Type for Availaibility Change of EQUIPMENT.

    :ivar equipment_ref: Reference to an EQUIPMENT.
    :ivar description: Description of EQUIPMENT.  (Unbounded since SIRI
        2.0)
    :ivar equipment_type_ref: Reference to a TYPE OF EQUIPMENT.
    :ivar validity_period: Period for which change to EQUIPMENT status
        applies applies. If omitted, indefinite period.
    :ivar equipment_status: Availability status of the EQUIPMENT.
        Default is 'notAvailable'.
    :ivar equipment_features: Service Features associated with
        equipment.
    :ivar extensions:
    """

    equipment_ref: Optional[EquipmentRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    equipment_type_ref: Optional[EquipmentTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentTypeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_status: EquipmentStatusEnumeration = field(
        default=EquipmentStatusEnumeration.NOT_AVAILABLE,
        metadata={
            "name": "EquipmentStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    equipment_features: Optional[
        "EquipmentAvailabilityStructure.EquipmentFeatures"
    ] = field(
        default=None,
        metadata={
            "name": "EquipmentFeatures",
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
    class EquipmentFeatures:
        """
        :ivar feature_ref: Service or Stop features associated with
            equipment. Recommended values based on TPEG are given in
            SIRI documentation and enumerated in the siri_facilities
            package.
        """

        feature_ref: list[FeatureRefStructure2] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
