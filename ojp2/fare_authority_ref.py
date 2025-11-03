from dataclasses import dataclass

from ojp2.fare_authority_ref_structure import FareAuthorityRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareAuthorityRef(FareAuthorityRefStructure):
    """
    Reference to a Fare Authority.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
