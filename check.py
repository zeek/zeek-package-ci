#!/usr/bin/env python3
from __future__ import print_function
from checks import check_all
import os
import sys

def main(pkg):
    results = check_all(pkg)
    ok = True
    for r in results:
        if r.ok:
            print (r.name, "OK")
        else:
            print (r.name, "FAIL")
            ok = False
        print ("Info:")
        for i in r.info:
            print(i)
        print()
        if r.errors:
            print ("Errors:")
            for e in r.errors:
                print(e)

    return ok

if __name__ == "__main__":
    pkg = sys.argv[1]
    if main(pkg):
        sys.exit(0)
    else:
        sys.exit(1)
