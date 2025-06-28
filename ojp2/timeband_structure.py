from dataclasses import dataclass

from ojp2.half_open_time_range_structure_1 import HalfOpenTimeRangeStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class TimebandStructure(HalfOpenTimeRangeStructure1):
    """
    Type for a timeband.
    """
