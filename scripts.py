import black
import sys
import logging
import typer
import pathlib
from isort import main as isort_main
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(show_time=False)],
)
logger = logging.getLogger("rich")
app = typer.Typer(
    name="scripts",
    help="Scripts collection for use poetry scripts",
    no_args_is_help=True,
    add_completion=False,
    pretty_exceptions_show_locals=False,
)
weatherbot_level_dir = pathlib.Path(__file__).parent
weatherbot_source_dir = weatherbot_level_dir / "weatherbot"
weatherbot_pyproject = weatherbot_level_dir / "pyproject.toml"

WEATHERBOT_SOURCE_DIR = str(weatherbot_source_dir)
WEATHERBOT_PYPROJECT = str(weatherbot_pyproject)

COMMON_CHECK_DIRS = [
    WEATHERBOT_SOURCE_DIR,
]
common_check_dirs_str_joined = ", ".join(COMMON_CHECK_DIRS)


@app.command(help="Run formating")
def format() -> None:
    logger.info("Running isort in %s", common_check_dirs_str_joined)
    sys.argv = [
        "isort",
        *COMMON_CHECK_DIRS,
    ]
    isort_main.main()
    logger.info("Running black in %s", common_check_dirs_str_joined)
    sys.argv = [
        "black",
        *COMMON_CHECK_DIRS,
        "--config",
        WEATHERBOT_PYPROJECT,
    ]
    black.patched_main()
    logger.info(sys.argv)


@app.command(help="Run check linters")
def lint() -> None:
    logger.info("Running isort in %s", common_check_dirs_str_joined)
    sys.argv = [
        "isort",
        *COMMON_CHECK_DIRS,
        "--check-only",
        "--diff",
    ]
    isort_main.main()
    logger.info("Running black in %s", common_check_dirs_str_joined)
    sys.argv = [
        "black",
        "--check",
        *COMMON_CHECK_DIRS,
        "--config",
        WEATHERBOT_PYPROJECT,
    ]
    black.patched_main()


if __name__ == "__main__":
    app()
