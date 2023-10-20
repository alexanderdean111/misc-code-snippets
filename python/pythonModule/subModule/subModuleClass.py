#!/usr/bin/python3

import logging

class SubModuleClass:
    def __init__(self):
        self._logger = logging.getLogger("SubModuleClass")
        self._logger.info("initialized SubModuleClass")

    def classMethod(self, someInput):
        self._logger.info(f"called classMethod: {someInput}")
