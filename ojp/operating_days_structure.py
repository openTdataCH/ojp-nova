from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatingDaysStructure:
    """
    [TMv6] day of public transport operation of which the characteristics are
    defined in a specific SERVICE CALENDAR and which may last more than 24
    hours.

    :ivar from_value: Start date of period.
    :ivar to: End date of period.
    :ivar pattern: Bit pattern for operating days between start date and
        end date. The length of the pattern is equal to the number of
        days from start date to end date. A bit value of "1" indicates
        that an event actually happens on the day that is represented by
        the bit position.
    """
    from_value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    to: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pattern",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
            "pattern": r"[01]*",
        }
    )
