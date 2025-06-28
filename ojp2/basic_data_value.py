from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.computation_method_enum import ComputationMethodEnum
from ojp2.extension_type import ExtensionType
from ojp2.group_of_locations import GroupOfLocations
from ojp2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class BasicDataValue:
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    computational_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fault: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fault_reason: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "faultReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pertinent_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "pertinentLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "basicDataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
