from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareAuthorityRefStructure:
    """
    Reference to a Fare Authority ([a specialisation of an ORGANISATION in TMv6]
    ORGANISATION which has the RESPONSIBILITY ROLE for the definition of FARE
    PRODUCTs).
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
