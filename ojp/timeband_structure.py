from dataclasses import dataclass
from ojp.half_open_time_range_structure_2 import HalfOpenTimeRangeStructure2

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class TimebandStructure(HalfOpenTimeRangeStructure2):
    """
    Type for a timeband.
    """
