from dataclasses import dataclass
from ojp.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CodeWithAuthorityType(CodeType):
    """
    gml:CodeWithAuthorityType requires that the codeSpace attribute is provided
    in an instance.
    """
