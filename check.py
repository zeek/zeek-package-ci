#!/usr/bin/env python3
from __future__ import print_function
from checks import check_all, check_all_dict
import json
import os
import sys

import argparse

def txt_main(pkg):
    print("Checking", pkg)
    results = check_all(pkg)
    ok = True
    for r in results:
        if r.ok:
            print (r.name, "OK")
        else:
            print (r.name, "FAIL")
            ok = False
        if r.info:
            print ("Info:")
            for i in r.info:
                print(i)
            print()
        if r.errors:
            print ("Errors:")
            for e in r.errors:
                print(e)
            print()
        if r.warnings:
            print ("Warnings:")
            for e in r.warnings:
                print(e)
            print()

    return ok


def json_main(pkg, quiet=False, pretty=False):
    indent = 4 if pretty else None

    res = check_all_dict(pkg)
    if res["ok"] == False or not quiet:
        print(json.dumps(res, indent=indent))
    return res["ok"]

def main():

    parser = argparse.ArgumentParser(description='Check bro packages')
    parser.add_argument('package', metavar='N', type=str,
                        help='bro package to check')
    parser.add_argument('--quiet', dest='quiet', action='store_true',
                        default=False,
                        help='be quiet')
    parser.add_argument('--json', dest='json', action='store_true',
                        default=False,
                        help='output using json')
    parser.add_argument('--pretty', dest='pretty', action='store_true',
                        default=False,
                        help='be pretty')

    args = parser.parse_args()

    if args.json:
        ret = json_main(args.package, args.quiet, args.pretty)
    else:
        ret = txt_main(args.package)

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
