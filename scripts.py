import logging
import pathlib
import sys
import black

from isort import main as isort_main
from mypy.main import main as mypy_main

TOP_LEVEL_DIR = pathlib.Path(__file__).parent
logging.basicConfig(
    level=logging.INFO, format="%(levelname)-7s %(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def lint():
    if len(sys.argv) > 1:
        logger.warning("lint not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    logger.info("Running isort")
    sys.argv = [
        "isort",
        str(TOP_LEVEL_DIR / "weatherbot"),
        "--check-only",
        "--diff",
    ]
    isort_main.main()
    logger.info("Isort check passed")

    logger.info("Running black")
    sys.argv = [
        "black",
        str(TOP_LEVEL_DIR / "weatherbot"),
        "--config",
        str(TOP_LEVEL_DIR / "pyproject.toml"),
        "--check",
        "--diff",
        "--color",
    ]
    try:
        black.patched_main()
    except SystemExit as e:
        if e.code != 0:
            raise
    logger.info("Black check passed")

    logger.info("Running mypy")

    mypy_main(
        args=[
            str(TOP_LEVEL_DIR / "weatherbot"),
            "--config-file",
            str(TOP_LEVEL_DIR / "pyproject.toml"),
        ],
        clean_exit=True,
    )

    logger.info("Mypy check passed")


def format():
    if len(sys.argv) > 1:
        logger.warning("format not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    sys.argv = [
        "isort",
        str(TOP_LEVEL_DIR / "weatherbot"),
    ]
    isort_main.main()

    sys.argv = [
        "black",
        str(TOP_LEVEL_DIR / "weatherbot"),
        "--config",
        str(TOP_LEVEL_DIR / "pyproject.toml"),
    ]
    black.patched_main()
