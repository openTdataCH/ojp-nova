from dataclasses import dataclass, field
from typing import List, Optional
from ojp.empty_type import EmptyType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityRequestPolicyStructure:
    """
    Type for Common Request Policy capabilities.

    :ivar national_language: National languages supported by service.
    :ivar translations: Whether producer can provide multiple
        translations of NL text elements  +SIRI 2.0
    :ivar gml_coordinate_format: Name of GML Coordinate format used for
        Geospatial points in responses.
    :ivar wgs_decimal_degrees: Geospatial coordinates are given as Wgs
        84 Latiude and longitude, decimial degrees of arc.
    """
    national_language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NationalLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    translations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Translations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    gml_coordinate_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "GmlCoordinateFormat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    wgs_decimal_degrees: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "WgsDecimalDegrees",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
