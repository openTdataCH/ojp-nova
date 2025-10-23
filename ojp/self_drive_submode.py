from dataclasses import dataclass, field
from ojp.self_drive_submodes_of_transport_enumeration import SelfDriveSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SelfDriveSubmode:
    """
    TPEG pti12 SelfDrive submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SelfDriveSubmodesOfTransportEnumeration = field(
        default=SelfDriveSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
