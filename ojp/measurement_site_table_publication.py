from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.header_information import HeaderInformation
from ojp.measurement_site_table import MeasurementSiteTable
from ojp.payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MeasurementSiteTablePublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measurement_site_table: List[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    measurement_site_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
