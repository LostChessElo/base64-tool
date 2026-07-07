import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from base64_tool.constants import (
    CONFIDENCE_THRESHOLD,
    EncodingFormat,
    PREVIEW_LENGTH,
)
from base64_tool.detectors import DetectionResult
from base64_tool.peeler import PeelResult
from base64_tool.util import safe_bytes_preview

console = Console(stderr=True)

def is_piped() -> bool:
    pass 

def write_raw(test: str) -> None:
    pass

def print_encoded(result: str, fmt: EncodingFormat) -> None:
    pass

def print_decoded(result: bytes) -> None:
    pass

def print_score_breakdown(score: dict[EncodingFormat, float]) -> None:
    pass

def print_detection(result: list[DetectionResult], *, verbose_scores: dict[EncodingFormat, float] | None = None) -> None:
    pass

def print_peel_result(result: PeelResult, *, verbose: bool = False) -> None:
    pass

def print_chain_result(steps: list[tuple[EncodingFormat, str]], final: str) -> None:
    pass

def _confidence_color(confidence: float) -> str:
    pass
