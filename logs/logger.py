import logging
import sys
from logging import Logger


def create_handler(handler: logging.Handler) -> logging.Handler:
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    handler.setFormatter(formatter)
    return handler


def get_logger(name: str = __name__, log_file: str = "logfile.log", log_level: int = logging.DEBUG) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        fh_file = create_handler(logging.FileHandler(log_file, encoding='utf-8'))
        logger.addHandler(fh_file)

        ch_console = create_handler(logging.StreamHandler(sys.stdout))
        logger.addHandler(ch_console)

    return logger
