#!/usr/bin/env python3
import os
import sys
from .types import CheckResult
from ..bro_parser import bro_files

NAME = "incorrect_file_extension"
DESCRIPTION = "Check if any loaded bro scripts have an extension other than .bro or .sig"

def check_incorrect_file_extension(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        fn, ext = os.path.splitext(f)
        if os.path.exists(f) and ext.lower() not in (".bro", ".sig"):
            bad.append(f)

    if not bad:
        return CheckResult(NAME, DESCRIPTION, True)
    
    msg = "Package loads files with incorrect extensions: {}".format(', '.join(bad))
    return CheckResult(NAME, DESCRIPTION, False, errors=[msg])
