#!/usr/bin/python3

import logging

class SubModuleClassTwo:
    def __init__(self):
        self._logger = logging.getLogger("SubModuleClassTwo")
        self._logger.info("initialized SubModuleClassTwo")

    def classMethod(self, someInput):
        self._logger.info(f"called classMethod: {someInput}")
