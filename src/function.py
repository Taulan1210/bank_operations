import json


def get_operations(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)