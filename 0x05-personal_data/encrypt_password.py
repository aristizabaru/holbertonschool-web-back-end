#!/usr/bin/env python3
import bcrypt
"""encrypt_password module"""


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
