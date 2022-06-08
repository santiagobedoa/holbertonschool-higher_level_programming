#!/usr/bin/python3
''' Module for write_file func '''


def write_file(filename="", text=""):
    with open(filename, "r", encoding="utf-8") as f:
        return f.write(text)
