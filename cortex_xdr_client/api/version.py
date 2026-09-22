from enum import IntEnum


class APIVersion(IntEnum):
    """Cortex XDR product version, independent of the version in each API path."""
    V3 = 3
    V5 = 5
