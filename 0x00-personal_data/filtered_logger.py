#!/usr/bin/env python3
"""
   returns the log message obfuscated
"""

import re
import logging
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is
    separating all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """returns logging.Logger object
    The logger should be named "user_data" and only log up to logging.INFO
    level. It should not propagate messages to other loggers. It should
    have a StreamHandler with RedactingFormatter as formatter.
    """
    userlog = logging.getLogger('user_data')
    userlog.setLevel(logging.Info)
    userlog.propagate = False
    sh = logging.StreamHandler()
    useFormat = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(useFormat)
    userlog.addHandler(sh)
    return userlog
