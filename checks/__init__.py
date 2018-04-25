#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
from checks.types import CheckResult

from checks.license import check_license
from checks.readme import check_readme

CHECKS = [
    check_license,
    check_readme,
]

def check_all(pkg):
    for c in CHECKS:
        res = c(pkg)
        yield res
