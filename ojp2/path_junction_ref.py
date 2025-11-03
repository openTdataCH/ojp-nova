from dataclasses import dataclass

from ojp2.path_junction_ref_structure import PathJunctionRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PathJunctionRef(PathJunctionRefStructure):
    """
    Reference to a PATH JUNCTION.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
