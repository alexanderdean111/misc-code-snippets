#!/usr/bin/python3

import sys
import logging
import importlib

logging.basicConfig(
    format="%(asctime)s | %(levelname)8s | %(name)s | %(module)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S%z",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(sys.stdout)],
)

_logger = logging.getLogger("pythonModuleStructure")

_logger.info(f"importing subModule")
from .subModule import *
