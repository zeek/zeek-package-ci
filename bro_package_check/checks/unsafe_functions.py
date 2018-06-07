#!/usr/bin/env python3
import os
import sys
from .types import CheckResult
from ..bro_parser import bro_files, bro_tokens

NAME = "unsafe_functions"

UNSAFE_FUNCTIONS = set([
    "system",
    "system_env",
    "piped_exec",
    "execute_with_notice",
    "sendmail",
    "open",
    "open_for_append",
])

def check_unsafe_functions(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        for n, line, tokens in bro_tokens(f):
            for token_type, token in tokens:
                if token_type == 'TOKEN' and token in UNSAFE_FUNCTIONS:
                    msg = "{}:{} unsafe function {}".format(f, n, token)
                    bad.append(msg)
    
    return CheckResult(NAME, ok=True, warnings=bad)
