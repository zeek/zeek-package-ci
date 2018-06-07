#!/usr/bin/env python3
import os
import string
import sys
from .types import CheckResult
from ..bro_parser import bro_files

NAME = "charset"
DESCRIPTION = "Check if any loaded bro scripts contain non ascii characters"

printable = set(string.printable)

def is_ascii(line):
    return all(c < 128 for c in line)

def check_charset(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for fn in loaded_files:
        if not os.path.exists(fn):
            continue
        with open(fn, 'rb') as f:
            for n, line in enumerate(f, start=1):
                if not is_ascii(line):
                    msg = "{}:{} non ascii characters".format(fn, n)
                    bad.append(msg)

    return CheckResult(NAME, DESCRIPTION, ok=True, warnings=bad)
