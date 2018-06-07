#!/usr/bin/env python3
import os
import sys
from .types import CheckResult

NAME = "license"
LICENSE_FILENAMES = ["LICENSE", "COPYING"]
DESCRIPTION = "Check if the package contains a license file"

def check_license(pkg):
    for fn in os.listdir(pkg):
        f, ext = os.path.splitext(fn)
        if f in LICENSE_FILENAMES:
            msg = "Found license {!r}".format(f)
            return CheckResult(NAME, DESCRIPTION, True, [msg])

    msg = "Could not find a license file. Checked for {} with any extension".format(','.join(LICENSE_FILENAMES))
    return CheckResult(NAME, DESCRIPTION, False, errors=[msg])
