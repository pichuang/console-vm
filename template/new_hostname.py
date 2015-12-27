#!/usr/bin/env python3
import os
hostname = input("New hostname: ")
ignore_file = ["new_hostname.py"]

# Reference: http://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
for dname, dirs, files in os.walk(os.getcwd()):
    for fname in files:
        if not fname in ignore_file:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace("template", hostname)
            with open(fpath, "w") as f:
                f.write(s)
            print("Change hostname in {0}".format(fpath))
