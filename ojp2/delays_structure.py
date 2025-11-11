from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.delay_band_enumeration import DelayBandEnumeration
from ojp2.delays_type_enum import DelaysTypeEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DelaysStructure:
    """
    Type for easement info.

    :ivar delay_band: Time band into which delay will fall.
    :ivar delay_type: Category of delay.
    :ivar delay: Additional journey time needed to overcome disruption.
    """

    delay_band: Optional[DelayBandEnumeration] = field(
        default=None,
        metadata={
            "name": "DelayBand",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "DelayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
