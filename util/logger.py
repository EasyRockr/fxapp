from functools import wraps
from typing import Callable
import logging

class Logger:
    def __init__(self):
        self.__logger = logging.getLogger("MyApp")
        if not self.__logger.handlers:
            formatter = '%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d - %(funcName)s) - %(message)s'
            logging.basicConfig(filename="my_app.log", level=logging.INFO, format=formatter)

    def get_logger(self):
        return self.__logger


def enable_logging(function_pointer: Callable):
    @wraps(function_pointer)
    def wrapper(*args, **kwargs):
        logger = Logger().get_logger()
        logger.info(f"Begin: [{function_pointer.__name__}]")
        logger.info(f"Args: {args} -- Kwargs: {kwargs}")
        try:
            result = function_pointer(*args, **kwargs)
            logger.info(f"End: [{function_pointer.__name__}]")
            return result
        except Exception as ex:
            logger.error(f"Exception in {function_pointer.__name__}: {ex}", exc_info=True)
            raise ex
    return wrapper
