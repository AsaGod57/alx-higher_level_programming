#!/usr/bin/python3
# 5-no_c.py
# Godsway Asamoah <gasamoah@wacci.ug.edu.gh>


def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
