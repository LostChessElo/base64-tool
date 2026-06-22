import sys
from pathlib import Path

import typer


def resolve_input_bytes(data: bytes | None, file: Path | None ) -> bytes:
    if file is not None:
        if not file.exists():
            raise typer.BadParameter(f"File not found: {file}")
        return file.read_bytes
    if data is not None:
        return data.encode("utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.buffer.read()
    raise typer.BadParameter("No input provided. Pass an argument, use --file, or use pipe stdin")


def resolve_input_text(data: bytes | None, file: Path | None) -> str:
    if file is not None:
        if not file.exists():
            raise typer.BadParameter(f"File not found: {file}")
        return file.read_text("utf-8").strip()
    if data is not None:
        return data.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    raise typer.BadParameter("No input provided. Pass an argument, use --file, or use pipe stdin")


def truncate() -> str:
    pass

def safe_bytes_preview() -> str:
    pass

def is_printable_text() -> bool:
    pass
