import typer
from pathlib import Path

from .filesystem import create_dirs_and_files

app = typer.Typer(help="scaffold-ai: project scaffolder")

__version__ = "0.0.1"


@app.command()
def version() -> None:
    typer.echo(__version__)


@app.command()
def init(
    name: str = typer.Argument(..., help="Name of the new project"),
    template: str = typer.Option(
        "python-simple-app",
        "--template",
        "-t",
        help="Template to use (e.g. python-simple-app, web-spa-js)",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing project directory if it already exists",
    ),
) -> None:
    """Initialize a new project from a template."""
    project_name = name
    base_dir = Path.cwd()
    project_dir = base_dir / project_name

    if project_dir.exists() and not force:
        typer.echo(
            f"Target directory '{project_dir}' already exists. "
            "Use --force to overwrite.",
            err=True,
        )
        raise typer.Exit(code=1)

    package_root = Path(__file__).resolve().parent.parent
    templates_root = package_root / "templates"
    template_path = templates_root / template / "base_tree.txt"

    if not template_path.exists():
        typer.echo(f"Template not found: {template_path}", err=True)
        raise typer.Exit(code=1)

    lines = template_path.read_text(encoding="utf-8").splitlines()
    create_dirs_and_files(base_dir, lines, project_name)
    typer.echo(f"Scaffolded '{project_name}' using template '{template}'.")
    

if __name__ == "__main__":
    app()
