#!/usr/bin/python3
# 8-multiple_returns.py
# Godsway Asamoah <gasamoah@wacci.ug.edu.gh>


def multiple_returns(sentence):

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
