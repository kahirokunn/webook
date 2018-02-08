import logging


class Log:

    @staticmethod
    def info(msg):
        logger = logging.getLogger('command')
        logger.info(msg)
