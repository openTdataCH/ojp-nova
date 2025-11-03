from dataclasses import dataclass

from ojp2.operating_day_ref_structure import OperatingDayRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatingDayRef(OperatingDayRefStructure):
    """
    Reference to an Operating Day.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
