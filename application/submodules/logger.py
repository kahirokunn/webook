from logging import getLogger

DEFAULT_LOGGER = 'webook_logger'


def critical(message, logger_name=DEFAULT_LOGGER) -> None:
    _logging('critical', message, logger_name, True)


def error(message, logger_name=DEFAULT_LOGGER) -> None:
    _logging('error', message, logger_name, True)


def warning(message, logger_name=DEFAULT_LOGGER) -> None:
    _logging('warning', message, logger_name, True)


def info(message, logger_name=DEFAULT_LOGGER) -> None:
    _logging('info', message, logger_name, False)


def _logging(log_type, message, logger_name, exc_info_flg=False) -> None:
    logger = getLogger(logger_name)
    func = getattr(logger, log_type)

    if isinstance(message, list) or isinstance(message, tuple):
        for m in message:
            func(m, exc_info=exc_info_flg)
    else:
        func(message, exc_info=exc_info_flg)
