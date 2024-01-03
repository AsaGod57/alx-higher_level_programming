#!/usr/bin/python3
# 101-remove_char_at.py
# Godsway Asamoah <gasamoah@wacci.ug.edu.gh>


def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
