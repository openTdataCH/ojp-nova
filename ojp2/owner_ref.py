from dataclasses import dataclass

from ojp2.owner_ref_structure import OwnerRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OwnerRef(OwnerRefStructure):
    """
    Reference to an  ORGANISATION with ownership as the RESPONSIBILITY ROLE.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
