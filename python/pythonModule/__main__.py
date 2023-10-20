#!/usr/bin/python3

import sys
import logging

# logging basic config already defined in __init__.py, so just grab the logger
_logger = logging.getLogger("pythonModuleStructure")

_logger.info(f"importing SubModuleClass from subModule")
from .subModule import SubModuleClass

_logger.info("initializing SubModuleClass")
m = SubModuleClass()

_logger.info("calling known method for SubModuleClass")
m.classMethod("called known class method")

from .subModuleTwo import SubModuleClassTwo

_logger.info("initializing SubModuleClassTwo")
m = SubModuleClassTwo()

_logger.info("calling known method for SubModuleClassTwo")
m.classMethod("called known class method")

