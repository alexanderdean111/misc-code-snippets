#!/usr/bin/python3

import logging
import sys

logging.basicConfig(
    format="%(asctime)s | %(levelname)8s | %(name)s | %(filename)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S%z",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(sys.stdout)],
)

# get a logger object
_logger = logging.getLogger("example logger")

_logger.debug("debug")
_logger.info("info")
_logger.warning("warning")
_logger.error("error")
_logger.critical("critical")
