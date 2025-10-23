from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlTime
from nova.wochen_tag import WochenTag

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StreckenSperre:
    """
    :ivar meldung_ref: @Deprecated Will be removed in NOVA 15. Use
        "meldungRefs" instead.
    :ivar meldung_refs:
    :ivar umsteige_punkt_uic:
    :ivar strecken_sperre_gueltigkeiten: List contains information about
        the durations of a Streckensperre. Multiple child elements means
        AND
    """
    meldung_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "meldungRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    meldung_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "tokens": True,
        }
    )
    umsteige_punkt_uic: List[int] = field(
        default_factory=list,
        metadata={
            "name": "umsteigePunktUIC",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_sperre_gueltigkeiten: Optional["StreckenSperre.StreckenSperreGueltigkeiten"] = field(
        default=None,
        metadata={
            "name": "streckenSperreGueltigkeiten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class StreckenSperreGueltigkeiten:
        strecken_sperre_gueltigkeit: List["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit"] = field(
            default_factory=list,
            metadata={
                "name": "streckenSperreGueltigkeit",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 1,
            }
        )

        @dataclass
        class StreckenSperreGueltigkeit:
            """
            :ivar wochen_tage: Weeks days within begin and end when the
                streckenSperre is active. "wochenTage" limits "beginn"
                and "ende" to the explicit week days defined.
            :ivar sperr_zeiten: Times within begin and end andweek days
                when the Streckensperre is active. "sperrZeiten" limits
                the Streckensperre to the explicit times defined here.
            :ivar beginn:
            :ivar ende:
            """
            wochen_tage: Optional["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.WochenTage"] = field(
                default=None,
                metadata={
                    "name": "wochenTage",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            sperr_zeiten: Optional["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.SperrZeiten"] = field(
                default=None,
                metadata={
                    "name": "sperrZeiten",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            beginn: Optional[XmlDateTime] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                }
            )
            ende: Optional[XmlDateTime] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                }
            )

            @dataclass
            class WochenTage:
                wochen_tag: List[WochenTag] = field(
                    default_factory=list,
                    metadata={
                        "name": "wochenTag",
                        "type": "Element",
                        "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                        "min_occurs": 1,
                    }
                )

            @dataclass
            class SperrZeiten:
                sperr_zeit: List["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.SperrZeiten.SperrZeit"] = field(
                    default_factory=list,
                    metadata={
                        "name": "sperrZeit",
                        "type": "Element",
                        "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class SperrZeit:
                    beginn_zeit: Optional[XmlTime] = field(
                        default=None,
                        metadata={
                            "name": "beginnZeit",
                            "type": "Element",
                            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                            "required": True,
                        }
                    )
                    ende_zeit: Optional[XmlTime] = field(
                        default=None,
                        metadata={
                            "name": "endeZeit",
                            "type": "Element",
                            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                            "required": True,
                        }
                    )
