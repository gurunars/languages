#!/usr/bin/python
import os

current_dir = os.path.abspath(os.curdir)

for tfile in os.listdir(current_dir):
    if not tfile.endswith(".csv"):
        continue
    tfile = os.path.join(current_dir, tfile)
    with open(tfile) as f:
        i = 1
        for line in f.readlines():
            i += 1
            errors = []
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
