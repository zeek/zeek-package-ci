#!/usr/bin/env python3
import os
import sys
from .types import CheckResult

from .license import check_license
from .readme import check_readme
from .build_command import check_build_command
from .incorrect_file_extension import check_incorrect_file_extension
from .expensive_events import check_expensive_events
from .unsafe_functions import check_unsafe_functions
from .charset import check_charset

CHECKS = [
    check_license,
    check_readme,
    check_build_command,
    check_incorrect_file_extension,
    check_expensive_events,
    check_unsafe_functions,
    check_charset,
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
