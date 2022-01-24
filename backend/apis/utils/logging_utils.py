"""
Universal logger throughout microservice
"""
# Python imports
import logging
import sys


def get_logger(name: str = "backend") -> logging.Logger:
    """Instantiate Logger object

    Args:
        name: Name of the logger that is seen in output

    Returns:
        Logger object
    """
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    return logging.getLogger(name)
