#!/usr/bin/python3

import sys
import logging

logging.basicConfig(
    format="%(asctime)s | %(levelname)8s | %(name)s | %(module)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S%z",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(sys.stdout)],
)

_logger = logging.getLogger("subModule")

_logger.info(f"importing SubModuleClass")
from .subModuleClass import SubModuleClass
_logger.info(f"imported subModule.SubModuleClass: {SubModuleClass}")
