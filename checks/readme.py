#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult

NAME = "readme"
README_FILENAMES = ["README"]

def check_readme(pkg):
    for fn in os.listdir(pkg):
        f, ext = os.path.splitext(fn)
        if f in README_FILENAMES:
            msg = "Found readme {!r}".format(fn)
            return CheckResult(NAME, True, [msg])

    msg = "Could not find a readme file. Checked for {!r} with any extension".format(README_FILENAMES)
    return CheckResult(NAME, False, errors=[msg])
