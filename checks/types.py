#!/usr/bin/env python3

class CheckResult():
    def __init__(self, name, ok=True, info=None, errors=None):
        self.name = name
        self.ok = ok
        self.info = [] if info is None else info
        self.errors = [] if errors is None else errors

    def __repr__(self):
        return "CheckResult({0.ok!r}, {0.info!r}, {0.errors!r})".format(self)

    def to_json(self):
        return {
            "name": self.name,
            "ok": self.ok,
            "info": self.info,
            "errors": self.errors,
        }
