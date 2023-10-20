#!/usr/bin/python3

import sys
import logging

# logging basic config already defined in __init__.py, so just grab the logger
_logger = logging.getLogger("subModule")
_logger.info(f"in __main__.py")
