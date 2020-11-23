#!/usr/bin/python
import os
from os import curdir


def validate_file(path):
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
            print("Errors @ %s" % tfile)
            for error in errors:
                print(error)
            print("")


curdir = os.path.abspath(os.curdir)


for language in os.listdir(curdir):
    for 

for tfile in os.listdir(current_dir):
    if not tfile.endswith(".csv"):
        continue
    tfile = os.path.join(current_dir, tfile)
