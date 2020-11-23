#!/usr/bin/python
import os
from os import curdir


def validate_collection(path):
    for subpath in os.listdir(path):
        validate_set(os.path.join(path, subpath))
        

def validate_set(path):
    if not path.endswith(".csv"):
        return
    with open(path) as f:
        errors = []
        for i, line in enumerate(f.readlines()):
            if not line:
                errors.append("Blank line @ %d" % i)
                continue
            commas = line.count(",")
            if commas == 0:
                errors.append("Line has no commas @ %d" % i)
                continue
            elif commas > 1:
                errors.append("Line has too many commas @ %d" % i)
                continue
            if line.count("  "):
                errors.append("Line has too many spaces in a row @ %d" % i)
        if errors:
            print("Errors @ %s" % path)
            for error in errors:
                print(error)
            print("")


curdir = os.path.abspath(os.curdir)


for subdir in os.listdir(curdir):
    if subdir.startswith("."):
        continue
    full_path = os.path.join(curdir, subdir)
    if not os.path.isdir(full_path):
        continue
    validate_collection(full_path)