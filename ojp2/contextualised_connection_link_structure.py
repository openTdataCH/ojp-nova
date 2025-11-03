from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.stop_point_name import StopPointName
from ojp2.stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ContextualisedConnectionLinkStructure:
    """Connection between two stops within a connection area.

    Used within the context of one or other end.

    :ivar connection_link_code: Identifier of CONNECTION LINk.
    :ivar stop_point_ref:
    :ivar stop_point_name:
    :ivar default_duration: Default time (Duration) needeed to traverse
        SERVICE JOURNEY INTERCHANGE from feeder to distributor.
    :ivar frequent_traveller_duration: Time needeed by a traveller whis
        is familiar with SERVICE JOURNEY INTERCHANGE to traverse it. If
        absent, use DefaultDuration.
    :ivar occasional_traveller_duration: Time needeed by a traveller
        whis is not familiar with SERVICE JOURNEY INTERCHANGE to
        traverse it. If absent, use DefaultDuration and a standard
        weighting.
    :ivar impaired_access_duration: Time needeed by a traveller wos is
        mobility impaired to traverse SERVICE JOURNEY INTERCHANGE. If
        absent, use DefaultDuration and a standard impaired travel
        speed.
    """

    connection_link_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: Optional[StopPointName] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DefaultDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    frequent_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequentTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occasional_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OccasionalTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impaired_access_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ImpairedAccessDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
