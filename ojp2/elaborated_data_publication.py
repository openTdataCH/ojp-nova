from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.elaborated_data import ElaboratedData
from ojp2.extension_type import ExtensionType
from ojp2.header_information import HeaderInformation
from ojp2.payload_publication import PayloadPublication
from ojp2.reference_settings import ReferenceSettings

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ElaboratedDataPublication(PayloadPublication):
    forecast_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "forecastDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_default: Optional[float] = field(
        default=None,
        metadata={
            "name": "periodDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
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
    reference_settings: Optional[ReferenceSettings] = field(
        default=None,
        metadata={
            "name": "referenceSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    elaborated_data: list[ElaboratedData] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    elaborated_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
