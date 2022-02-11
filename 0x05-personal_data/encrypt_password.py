#!/usr/bin/env python3
"""encrypt_password module"""
from xmlrpc.client import Boolean
import bcrypt


def hash_password(password: str) -> bytes:
    """turn password string to salted, hashed password byte string

    Args:
        password (str): password

    Returns:
        bytes: hashed password
    """
    byte_password = password.encode('utf-8')
    hashed = bcrypt.hashpw(byte_password, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> Boolean:
    """validate that the provided password matches the hashed password

    Args:
        hashed_password (bytes): hashed password
        password (str): string password

    Returns:
        Boolean: True if it matches, False if it does not
    """
    byte_password = password.encode('utf-8')
    return bcrypt.checkpw(byte_password, hashed_password)
