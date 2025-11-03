from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.header_information import HeaderInformation
from ojp2.payload_publication import PayloadPublication
from ojp2.site_measurements import SiteMeasurements

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MeasuredDataPublication(PayloadPublication):
    measurement_site_table_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    site_measurements: list[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measured_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
