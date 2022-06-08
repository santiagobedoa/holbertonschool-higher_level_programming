#!/usr/bin/python3
''' Module for load_from_json_file func '''
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
