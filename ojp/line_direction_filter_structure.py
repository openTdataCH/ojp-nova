from dataclasses import dataclass, field
from typing import List, Optional
from ojp.line_direction_structure import LineDirectionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LineDirectionFilterStructure:
    """
    Filter for in/exclusion of lines (and directions).

    :ivar line: Reference a GROUP of DIRECTIONs  of the ROUTEs belonging
        to the same LINE created  for the purpose of filtering and
        organising timetables..
    :ivar exclude: Whether lines in list are to include or exclude from
        search. Default is exclude.
    """
    line: List[LineDirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
