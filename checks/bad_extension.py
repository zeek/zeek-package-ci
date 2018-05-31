#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult
from checks.bro_parser import bro_files

NAME = "bad_extension"

def check_bad_extension(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        fn, ext = os.path.splitext(f)
        if ext.lower() not in (".bro", ".sig"):
            bad.append(f)

    if not bad:
        return CheckResult(NAME, True)
    
    msg = "Package contains files with incorrect extensions: {}".format(', '.join(bad))
    return CheckResult(NAME, False, errors=[msg])