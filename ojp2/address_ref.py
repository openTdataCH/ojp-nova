from dataclasses import dataclass

from ojp2.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AddressRef(AddressRefStructure):
    """
    Reference to an Address.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
