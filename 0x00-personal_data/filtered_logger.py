#!/usr/bin/env python3
"""Module for function that returns a log message obfuscated."""
import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates specific fields in a log message."""
    pattern = f'({"|".join(fields)})=([^"{separator}"]*)'
    return re.sub(pattern, lambda m: f'{m.group(1)}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records"""
        original_msg = record.getMessage()
        filtered_msg = filter_datum(
            self.fields, self.REDACTION, original_msg, self.SEPARATOR)
        record.msg = filtered_msg
        return super(RedactingFormatter, self).format(record)
