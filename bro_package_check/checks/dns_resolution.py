#!/usr/bin/env python3
import os
import sys
from .types import CheckResult
from ..bro_parser import bro_files, bro_tokens
import socket

NAME = "dns_resolution"
DESCRIPTION = "Check if any loaded bro scripts are relying on internal DNS resolution"

def is_hostname(s):
    #If it doesn't have ANY dots, it's not a hostname
    if '.' not in s:
        return False
    #If it's a float it's not a hostname
    try:
        float(s)
        return False
    except ValueError:
        pass

    #If it's an IPV4 address, it's not a hostname
    try:
        socket.inet_aton(s)
        return False
    except socket.error:
        pass

    return True

def check_dns_resolution(pkg):
    loaded_files = bro_files(pkg)
    bad = []
    for f in loaded_files:
        for n, line, tokens in bro_tokens(f):
            for token_type, token in tokens:
                if token_type == 'TOKEN' and is_hostname(token):
                    msg = "{}:{} dns resolution for {}".format(f, n, token)
                    bad.append(msg)
    
    return CheckResult(NAME, DESCRIPTION, ok=True, warnings=bad)
