import logging
import os
from logging import handlers


def init_logger(file_name=None, directory="./", level=logging.INFO, when="D", backup_count=10):
    logger = logging.getLogger()
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    format_str = logging.Formatter(fmt)
    logger.setLevel(level)
    sh = logging.StreamHandler()
    sh.setFormatter(format_str)
    logger.addHandler(sh)

    if file_name is not None:
        file_path = os.path.join(directory, file_name)
        th = handlers.TimedRotatingFileHandler(filename=file_path, when=when, backupCount=backup_count, encoding='utf-8')
        th.setFormatter(format_str)
        logger.addHandler(th)


if __name__ == "__main__":
    init_logger(file_name="test.log", directory="./")
    logging.info("hello")