!/usr/bin/python3
# 8-uppercase.py
# Godsway Asamoah <gasamoah@wacci.ug.edu.gh>


def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
