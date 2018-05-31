#!/usr/bin/env python3
import os
import sys
from checks.types import CheckResult
from checks.bro_parser import bro_files, bro_tokens

NAME = "bad_events"

BAD_EVENTS = set([
    "new_packet",
])

def check_bad_events(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        for n, line, tokens in bro_tokens(f):
            for token_type, token in tokens:
                if token_type == 'TOKEN' and token in BAD_EVENTS:
                    msg = "{}:{} bad event {}".format(f, n, token)
                    bad.append(msg)
    
    return CheckResult(NAME, bad == [], errors=bad)
