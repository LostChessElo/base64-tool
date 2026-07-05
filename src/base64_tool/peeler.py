from dataclasses import dataclass

from base64_tool.constants import (
    CONFIDENCE_THRESHOLD,
    PEEL_MAX_DEPTH,
)

@dataclass(frozen=True, slots=True)
class PeelLayer:
    pass

@dataclass(frozen=True, slots=True)
class PeelResult:
    pass

def peel(data: str, *, max_depth: int = PEEL_MAX_DEPTH, threshold: float = CONFIDENCE_THRESHOLD, verbose: bool = False) -> PeelResult:
    pass
