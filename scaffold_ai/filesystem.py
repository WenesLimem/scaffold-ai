from pathlib import Path
from typing import Iterable


def create_dirs_and_files(base: Path, lines: Iterable[str], project_name: str) -> None:
    """
    Simple parser for base_tree.txt.
    Creates directories and empty files relative to base directory.
    """
    current_dir_stack: list[tuple[int, Path]] = []

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        name = line.strip()

        if name.startswith("{project_name}"):
            rel = name.format(project_name=project_name).rstrip("/\\")
            path = base / rel
            path.mkdir(parents=True, exist_ok=True)
            current_dir_stack = [(indent, path)]
            continue

        while current_dir_stack and current_dir_stack[-1][0] >= indent:
            current_dir_stack.pop()

        parent = current_dir_stack[-1][1] if current_dir_stack else base

        if name.endswith("/"):
            dir_path = parent / name.rstrip("/\\")
            dir_path.mkdir(parents=True, exist_ok=True)
            current_dir_stack.append((indent, dir_path))
        else:
            file_path = parent / name
            file_path.parent.mkdir(parents=True, exist_ok=True)
            if not file_path.exists():
                file_path.write_text("", encoding="utf-8")
