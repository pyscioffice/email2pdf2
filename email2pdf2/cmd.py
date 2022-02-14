import logging
import sys
import os
from sys import platform as _platform
from email2pdf2.email2pdf2 import call_main


def setup_logger():
    logger_setup = logging.getLogger("email2pdf2")
    logger_setup.propagate = False
    logger_setup.setLevel(logging.DEBUG)

    syserr_handler_setup = logging.StreamHandler(stream=sys.stderr)
    syserr_handler_setup.setLevel(logging.WARNING)
    syserr_formatter = logging.Formatter('%(levelname)s: %(message)s')
    syserr_handler_setup.setFormatter(syserr_formatter)
    logger_setup.addHandler(syserr_handler_setup)

    if _platform == "linux" or _platform == "linux2":
        SYSLOG_ADDRESS = '/dev/log'
    elif _platform == "darwin":
        SYSLOG_ADDRESS = '/var/run/syslog'
    else:
        logger_setup.warning("I don't know this platform (" + _platform + "); cannot log to syslog.")
        SYSLOG_ADDRESS = None

    if SYSLOG_ADDRESS and os.path.exists(SYSLOG_ADDRESS):
        syslog_handler_setup = logging.handlers.SysLogHandler(address=SYSLOG_ADDRESS)
        syslog_handler_setup.setLevel(logging.INFO)
        SYSLOG_FORMATTER = logging.Formatter('%(pathname)s[%(process)d] %(levelname)s %(lineno)d %(message)s')
        syslog_handler_setup.setFormatter(SYSLOG_FORMATTER)
        logger_setup.addHandler(syslog_handler_setup)
    else:
        syslog_handler_setup = None
    return syslog_handler_setup, syserr_handler_setup


def main():
    syslog_handler_setup, syserr_handler_setup = setup_logger()
    call_main(sys.argv, syslog_handler_setup, syserr_handler_setup)


if __name__ == "__main__":
    main()
