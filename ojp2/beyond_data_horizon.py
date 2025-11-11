from dataclasses import dataclass

from ojp2.beyond_data_horizon_error_structure import (
    BeyondDataHorizonErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BeyondDataHorizon(BeyondDataHorizonErrorStructure):
    """Error: Data period or subscription period is outside of period covered by service."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
