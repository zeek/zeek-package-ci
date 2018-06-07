#!/usr/bin/env python3
import os
import sys
from .types import CheckResult

NAME = "readme"
README_FILENAMES = ["README"]
DESCRIPTION = "Check if the package contains a README"

def check_readme(pkg):
    for fn in os.listdir(pkg):
        f, ext = os.path.splitext(fn)
        if f in README_FILENAMES:
            msg = "Found readme {!r}".format(fn)
            return CheckResult(NAME, DESCRIPTION, True, [msg])

    msg = "Could not find a readme file. Checked for {} with any extension".format(','.join(README_FILENAMES))
    return CheckResult(NAME, DESCRIPTION, False, errors=[msg])
