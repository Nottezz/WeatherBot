import logging
import pathlib
import sys
import black

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

top_level_dir = pathlib.Path(__file__).parent


def lint():
    if len(sys.argv) > 1:
        logger.warning("lint not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    sys.argv = [
        "black",
        str(top_level_dir / "weathebot"),
        "--config",
        "./pyproject.toml",
        "--diff",
        "--color",
    ]
    black.patched_main()


def format():
    if len(sys.argv) > 1:
        logger.warning("format not support arguments")
        logger.warning("Ignoring arguments: %s", sys.argv[1:])

    sys.argv = [
        "black",
        str(top_level_dir / "weathebot"),
        "--config",
        "./pyproject.toml",
    ]
    black.patched_main()
