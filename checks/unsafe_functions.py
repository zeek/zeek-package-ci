#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult

NAME = "unsafe_functions"

def check_unsafe_functions(pkg):
    return CheckResult(NAME, True)
