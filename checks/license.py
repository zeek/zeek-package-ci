#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
from checks.types import CheckResult

NAME = "license"
LICENSE_FILENAMES = ["LICENSE", "COPYING"]

def check_license(pkg):
    for fn in os.listdir(pkg):
        f, ext = os.path.splitext(fn)
        if f in LICENSE_FILENAMES:
            msg = "Found license {!r}".format(f)
            return CheckResult(NAME, True, [msg])

    msg = "Could not find a license file. Checked for {!r} with any extension".format(LICENSE_FILENAMES)
    return CheckResult(NAME, False, errors=[msg])
