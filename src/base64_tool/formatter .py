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
    return not sys.stdout.isatty()

def write_raw(text: str) -> None:
    sys.stdout.write(text)
    sys.stdout.flush()

def print_encoded(result: str, fmt: EncodingFormat) -> None:
    if is_piped():
        write_raw(result)
        return
    panel = Panel(
        Text(result,
             style = "green"),
        title = f"[bold cyan]{fmt.value}[/bold cyan] encoded",
        border_style = "cyan",
    )
    console.print(panel)

def print_decoded(result: bytes) -> None:
    preview = safe_bytes_preview(result, length = 4096)
    if is_piped():
        write_raw(preview)
        return
    panel = Panel(
        Text(preview,
             style = "green"),
        title = "[bold cyan]Decoded[/bold cyan]",
        border_style = "cyan",
    )
    console.print(panel)

def print_score_breakdown(scores: dict[EncodingFormat, float]) -> None:
    table = Table(
        title = "Score Breakdown",
        show_header = True,
        header_style = "bold magenta",
    )
    table.add_column("Format", style = "cyan", min_width = 10)
    table.add_column(
        "Score",
        justify = "right",
        min_width = 8,
    )
    table.add_column("Status", min_width = 10)

    sorted_scores = sorted(
        scores.items(),
        key = lambda x: x[1],
        reverse = True,
    )
    for fmt, score in sorted_scores:
        color = _confidence_color(score)
        if score >= CONFIDENCE_THRESHOLD:
            status = "[green]detected[/green]"
        elif score > 0:
            status = "[yellow]below threshold[/yellow]"
        else:
            status = "[dim]no match[/dim]"
        table.add_row(
            fmt.value,
            f"[{color}]{score:.0%}[/{color}]",
            status,
        )

    console.print(table)

def print_detection(results: list[DetectionResult], *, verbose_scores: dict[EncodingFormat, float] | None = None) -> None:
    if verbose_scores is not None:
        print_score_breakdown(verbose_scores)
        console.print()

    if not results:
        console.print("[yellow]No encoding format detected.[/yellow]")
        return

    table = Table(
        title = "Detection Results",
        show_header = True,
        header_style = "bold magenta",
    )
    table.add_column("Format", style = "cyan", min_width = 10)
    table.add_column(
        "Confidence",
        justify = "right",
        style = "green",
        min_width = 12,
    )
    table.add_column("Decoded Preview", style = "dim")

    for result in results:
        confidence_str = f"{result.confidence:.0%}"
        preview = ""
        if result.decoded is not None:
            preview = safe_bytes_preview(
                result.decoded,
                PREVIEW_LENGTH,
            )
        table.add_row(
            result.format.value,
            confidence_str,
            preview,
        )

    console.print(table)


def print_peel_result(result: PeelResult, *, verbose: bool = False) -> None:
    pass

def print_chain_result(steps: list[tuple[EncodingFormat, str]], final: str) -> None:
    pass

def _confidence_color(confidence: float) -> str:
    pass
