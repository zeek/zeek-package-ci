#!/usr/bin/env python3
import configparser
import subprocess
import json
import os
import pprint
import sys

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


AGGREGATE_PATH = os.path.expanduser("~/.bro-pkg/scratch/aggregate.meta")

def load_aggregate(path=AGGREGATE_PATH):
    #subprocess.check_call(["bro-pkg", "refresh"])
    metadata_parser = configparser.RawConfigParser()
    if not metadata_parser.read(path):
        raise Exception("Can't parse {}".format(path))
    for p, info in metadata_parser.items():
        if p == 'DEFAULT': continue
        info_dict = dict(info.items())
        info_dict['name'] = p
        yield info_dict

def package_dir(package):
    name = package["name"]
    dir_name = name.replace("/","_")
    return dir_name

def clone(package):
    name = package["name"]
    dir_name = package_dir(package)
    if os.path.exists(dir_name):
        with cd(dir_name):
            subprocess.check_call(["git", "pull"])
    else:
        print("Cloning", name)
        subprocess.check_call(["git", "clone", package["url"], dir_name])


def clone_all():
    metadata = load_aggregate()
    for package in metadata:
        print(package['name'], package['description'])
        pprint.pprint(package)
        print()
        clone(package)

def current_version(package):
    clone_dir = package_dir(package)
    with cd(clone_dir):
        rev = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode()
    return rev

def test(package, bro_version='2.5.3'):
    version = current_version(package)
    print("\n-----------------------------------------------")
    print("Testing {} Version {}".format(package['name'], version))

    cur = os.getcwd()
    clone_dir = package_dir(package)
    host_dir = os.path.join(cur, clone_dir)
    container_dir = "/package/{}".format(clone_dir)
    bind_mount = "{}:{}".format(host_dir, container_dir)

    subprocess.call(["docker", "run", "-t", "-i", "--rm",
        "-v", bind_mount,
        "broplatform/bro:{}-dev".format(bro_version),
        "bro-pkg", "test", container_dir])

def test_all(bro_version):
    metadata = load_aggregate()
    for package in metadata:
        if 'test_command' in package:
            test(package, bro_version)

if __name__ == "__main__":
    if sys.argv[1] == 'clone':
        clone_all()

    if sys.argv[1] == 'test':
        try:
            version = sys.argv[2]
        except:
            version = '2.5.3'
        test_all(bro_version=version)
