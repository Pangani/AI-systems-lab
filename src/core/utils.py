# Re-usable code to avoid repetition across the project

from pathlib import Path

def ensure_dir(path: Path) -> None:
    """Ensure that a directory exists."""
    path.mkdir(parents=True, exist_ok=True)
 