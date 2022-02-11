#!/usr/bin/env python3
"""filtered_logger module"""

import logging
import mysql.connector
import os
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class

    Args:
        fields (List[str]): fields to obfuscate

    Returns:
        RedactingFormatter: new RedactingFormatter object
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize new instance

        Args:
            fields (List[str]): fields to obfuscate
        """
        # create format simple format object with custom
        # attribute fields and method filter_datum()
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """return a obfuscate string

        Args:
            record (logging.LogRecord): original debug string

        Returns:
            str: obfuscate string
        """
        # super().format(record) returns string formated
        # to then call filter_datum() to obfuscate it
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """return returns log message obfuscated

    Args:
        fields (List[str]): fields to obfuscate
        redaction (str): by what the field will be obfuscated
        message (str): log line to obfuscate
        separator (str): character separating all fields

    Returns:
        str: log message obfuscated
    """
    for field in fields:
        message = re.sub(r'{}=.+?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message


def get_logger() -> logging.Logger:
    """returns a new logger

    Returns:
        logging.Logger: new logger with RedactingFormatter() format
    """
    LOGGER_NAME = "user_data"

    new_logger = logging.getLogger(LOGGER_NAME)
    new_logger.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    new_logger.propagate = False
    new_logger.addHandler(stream_handler)

    return new_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a new mysql connector object

    Returns:
        mysql.connector.connection.MySQLConnectio: mysql connector object
    """
    config = {
        'user': os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        'password': os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        'host': os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        'database': os.getenv('PERSONAL_DATA_DB_NAME')
    }
    return mysql.connector.connect(**config)
