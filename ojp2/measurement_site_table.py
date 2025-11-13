from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.measurement_site_record import MeasurementSiteRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MeasurementSiteTable:
    measurement_site_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_site_table_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_record: list[MeasurementSiteRecord] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
