#!/usr/bin/env python3
"""
0x00. Personal data
"""
from typing import List
import re


def filter_datum(fields: List[str],
                redaction: str,
                message: str,
                separator: str):
    """_summary_

    Args:
        fields (List[str]): list of all fields to obfuscate
        redaction (str): a str
        message (str): the log line
        separator (str): separator
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message

