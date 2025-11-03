from dataclasses import dataclass

from ojp2.facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityRef(FacilityRefStructure):
    """
    Reference to a Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
