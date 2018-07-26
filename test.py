#!/usr/bin/env python
import glob
import unittest
from bro_package_check.check import check_all_dict
from bro_package_check.checks import (
    check_license,
    check_readme,
    check_build_command,
    check_incorrect_file_extension,
    check_expensive_events,
    check_unsafe_functions,
    check_charset,
    check_dns_resolution,
)

class TestBroPackageCheck(unittest.TestCase):

    def test_no_packages_raise_exceptions(self):
        for package in glob.glob("test_packages/*"):
            out = check_all_dict(package)

    def test_load_text_file(self):
        out = check_incorrect_file_extension("test_packages/load_txt_file")
        self.assertFalse(out.ok)

    def test_expensive_events(self):
        out = check_expensive_events("test_packages/new_packet")
        self.assertEqual(len(out.warnings), 1)
        self.assertIn('expensive event new_packet', out.warnings[0])

    def test_dns_resolution(self):
        out = check_dns_resolution("test_packages/dns_resolution")
        self.assertEqual(len(out.warnings), 1)
        self.assertIn('dns resolution for www.google.com', out.warnings[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
