from dataclasses import dataclass

from ojp2.navigation_path_ref_structure import NavigationPathRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class NavigationPathRef(NavigationPathRefStructure):
    """
    Reference to a NAVIGATION PATH.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
