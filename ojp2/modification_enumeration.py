from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class ModificationEnumeration(Enum):
    """Classification of modification as addition, deletion or revision.

    Enumerated value.

    :cvar NEW: This is a definition of a new entity.
    :cvar DELETE: This is a deletion of an existing entity.
    :cvar REVISE: This is a revision to an existing entity. All values
        are replaced.
    """

    NEW = "new"
    DELETE = "delete"
    REVISE = "revise"
