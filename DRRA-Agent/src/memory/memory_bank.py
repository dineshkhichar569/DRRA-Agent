from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any

from .disaster_context import DisasterContext

# Memory file is stored next to this module by default
_MEMORY_FILE = Path(__file__).resolve().parent / "disaster_memory.json"


def load_memory() -> List[Dict[str, Any]]:
    """
    Load the list of past disaster contexts from a JSON file.
    Returns an empty list if the file does not yet exist.
    """
    if not _MEMORY_FILE.exists():
        return []

    with _MEMORY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(records: List[Dict[str, Any]]) -> None:
    """
    Persist the full list of disaster contexts to disk.
    """
    with _MEMORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)


def add_disaster_to_memory(ctx: DisasterContext) -> None:
    """
    Append a new disaster context to the long-term memory store.
    """
    records = load_memory()
    records.append(ctx.__dict__)
    save_memory(records)
