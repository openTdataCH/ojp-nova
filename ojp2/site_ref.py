from dataclasses import dataclass

from ojp2.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SiteRef(SiteRefStructure):
    """
    Reference to a SITE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
