from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extension_type import ExtensionType
from ojp.measured_value import MeasuredValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class SiteMeasurements:
    measurement_site_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    measurement_time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measured_value: List["SiteMeasurements.MeasuredValue"] = field(
        default_factory=list,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )

    @dataclass
    class MeasuredValue(MeasuredValue):
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
