from dataclasses import dataclass

from ojp2.line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineRef(LineRefStructure):
    """
    Reference to a LINE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
