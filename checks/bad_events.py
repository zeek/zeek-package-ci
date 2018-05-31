#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult

NAME = "bad_events"

def check_bad_events(pkg):
    return CheckResult(NAME, True)
