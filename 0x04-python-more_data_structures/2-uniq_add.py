#!/usr/bin/python3
# 2-uniq_add.py
# Godsway Asamoah <gasamoah@wacci.ug.edu.gh>


def uniq_add(my_list=[]):

    result = 0
    for x in set(my_list):
        result += x
    return (result)
