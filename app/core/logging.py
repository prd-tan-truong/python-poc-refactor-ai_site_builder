#  ! /usr/bin/python
#
#  Copyright (C) 2021 paradox.ai
#
#  Release: 2.2.8
#  @link olivia.paradox.ai
#
__author__ = "prd-tai-nguyen"
__date__ = "$May 26, 2023$"

import logging

from typing import Any, Final


_APP_NAME: Final[str] = "ai-site-builder"

logger: logging.Logger = logging.getLogger("tmp")


class Logger:
    prefix: str = f"[{_APP_NAME}]"

    @classmethod
    def info(cls, message: str, service_name: str) -> None:
        logger.info(message=message, prefix=f"{cls.prefix}[{service_name}]")

    @classmethod
    def debug(cls, message: str, service_name: str) -> None:
        logger.debug(message=message, prefix=f"{cls.prefix}[{service_name}]")

    @classmethod
    def warn(cls, message: str, service_name: str) -> None:
        logger.warn(message=message, prefix=f"{cls.prefix}[{service_name}]")

    @classmethod
    def error(cls, error_obj: Any, service_name: str) -> None:
        logger.error(error_obj=error_obj, prefix=f"{cls.prefix}[{service_name}]")
