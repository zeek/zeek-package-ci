#!/usr/bin/env python3
from __future__ import print_function
from checks import check_all, check_all_dict
import json
import os
import sys

def main(pkg):
    print("Checking", pkg)
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


def json_main(pkg):
    res = check_all_dict(pkg)
    print(json.dumps(res, indent=4))
    return res["ok"]

if __name__ == "__main__":
    pkg = sys.argv[1]
    if json_main(pkg):
        sys.exit(0)
    else:
        sys.exit(1)
