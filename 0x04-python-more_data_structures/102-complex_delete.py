#!/usr/bin/python3
# 102-complex_delete.py
# Godsway Asamoah


def complex_delete(a_dictionary, value):

    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)