#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult

from checks.license import check_license
from checks.readme import check_readme
from checks.build_command import check_build_command

CHECKS = [
    check_license,
    check_readme,
    check_build_command,
]

def check_all(pkg):
    for c in CHECKS:
        res = c(pkg)
        yield res

def check_all_dict(pkg):
    res = {"package": pkg, "checks": []}
    results = list(check_all(pkg))
    res["checks"] = [r.to_json() for r in results]
    res["ok"] = all(r.ok for r in results)
    return res
