#!/usr/bin/env python3
"""filtered_logger module"""

from typing import List
import re


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
