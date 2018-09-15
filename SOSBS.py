#!/usr/bin/python3

"""
S.O.S.B.S: The (S)kift(O)(S) (B)uild (S)ystem
"""

from pprint import pprint
from enum import Enum

import os
import sys
import json

# --- Utils ------------------------------------------------------------------ #

ESC = '\033['

BLACK = ESC + '30m'
RED = ESC + '31m'
GREEN = ESC + '32m'
YELLOW = ESC + '33m'
BLUE = ESC + '34m'
MAGENTA = ESC + '35m'
CYAN = ESC + '36m'
WHITE = ESC + '37m'

BRIGHT_BLACK = ESC + '30;1m'
BRIGHT_RED = ESC + '31;1m'
BRIGHT_GREEN = ESC + '32;1m'
BRIGHT_YELLOW = ESC + '33;1m'
BRIGHT_BLUE = ESC + '34;1m'
BRIGHT_MAGENTA = ESC + '35;1m'
BRIGHT_CYAN = ESC + '36;1m'
BRIGHT_WHITE = ESC + '37;1m'

RESET = ESC + '0m'

# --- Crosscompiler ---------------------------------------------------------- #


def crosscompiler_check():
    pass


def Crosscompiler_build():
    pass

# --- Utils ------------------------------------------------------------------ #

def join(a, b):
    return os.path.join(a, b)


def is_uptodate(outfile, infiles):
    if os.path.exists(outfile):
        pass

    return False


def get_files(locations, ext):
    files = []

    for root, _, filenames in os.walk(locations):
        for filename in filenames:
            if filename.endswith(ext):
                files.append(join(root, filename))

    return files

# --- Targets ---------------------------------------------------------------- #


class TargetTypes(Enum):
    INVALID = 0
    LIB = 1
    APP = 2
    KERNEL = 3
    MODULE = 4

    @staticmethod
    def FromStr(s):
        if s == "lib":
            return TargetTypes.LIB
        elif s == "app":
            return TargetTypes.APP
        elif s == "kernel":
            return TargetTypes.KERNEL
        elif s == "module":
            return TargetTypes.MODULE
        else:
            return TargetTypes.INVALID


class Target(object):
    def __init__(self, location, data):
        self.name = data["id"]
        self.type = TargetTypes.FromStr(data["type"])
        self.location = location

    def get_sources(self):
        pass

    def compile(self, source):
        pass

    def link(self):
        pass

    def build(self):
        for source in self.get_sources():
            if not self.compile(source):
                return False

        return self.link()


def list_targets(location):
    """

    """

    targets = {}

    for i in os.listdir(location):
        target_location = join(location, i)

        json_file = join(target_location, "manifest.json")

        if (os.path.exists(json_file)):
            data = json.loads(open(json_file).read())
            targets[data["id"]] = Target(target_location, data)

    return targets


# --- Action ----------------------------------------------------------------- #

def clean(target, targets):
    """Clean a target."""
    pass


def build(target, targets):
    """Build a target."""
    pass


def rebuild(target, targets):
    """Clean and build a target."""
    pass


def run(target, targets):
    """Start the kernel and the specified target."""
    pass


def info(target, targets):
    """Dump information about the target."""
    print(BRIGHT_WHITE + "Target " + target.name + ":" + RESET)
    print("\tType: " + str(target.type.name.lower()))
    print("\tDependencies: <TBD>")
    print("\tLocation: " + target.location)
    print("\tOutput: <TBD>")
    pass


actions = \
    {
        "build": build,
        "clean": clean,
        "rebuild": rebuild,
        "run": run,
        "info": info
    }


def clean_all(targets):
    """Clean all targets."""
    pass


def build_all(targets):
    """Build all tagets."""
    pass


def rebuild_all(targets):
    """Clean and build all targets."""
    pass


def help_command(targets):
    """Show this help message."""
    print(BRIGHT_WHITE + "S.O.S.B.S, version 2.0" + RESET)
    print("The skiftOS build system\n")

    print(BRIGHT_WHITE + "Usage :" + RESET + " ./SOSBS.py [action] targets...")
    print("        ./SOSBS.py [global action]")

    print("\n" + BRIGHT_WHITE + "Targets:" + RESET)
    print("   ", ', '.join(targets.keys()))

    print("\n" + BRIGHT_WHITE + "Actions:" + RESET)
    for act in actions:
        print("    %-12s %s" % (act, actions[act].__doc__))

    print("\n" + BRIGHT_WHITE + "Global actions:" + RESET)
    for act in global_actions:
        print("    %-12s %s" % (act, global_actions[act].__doc__))


def list_command(targets):
    """List all available targets."""
    # print(BRIGHT_WHITE + "Targets: " + RESET + ', '.join(targets.keys()))
    list_app(targets)
    list_lib(targets)
    list_other(targets)


def list_lib(targets):
    """List all available libraries."""
    libraries = {k: v for k, v in targets.items() if v.type == TargetTypes.LIB}
    print(BRIGHT_WHITE + "Libraries: " + RESET + ', '.join(libraries.keys()))
    pass


def list_app(targets):
    """List all available applications."""
    applications = {k: v for k, v in targets.items() if v.type == TargetTypes.APP}
    print(BRIGHT_WHITE + "Applications: " + RESET + ', '.join(applications.keys()))

def list_other(targets):
    """List all everithing else."""
    applications = {k: v for k, v in targets.items() if v.type != TargetTypes.APP and  v.type != TargetTypes.LIB}
    print(BRIGHT_WHITE + "Other: " + RESET + ', '.join(applications.keys()))


global_actions = \
    {
        "build-all": build_all,
        "clean-all": clean_all,
        "help": help_command,
        "list": list_command,
        "list-app": list_app,
        "list-lib": list_lib,
        "list-other": list_other,
        "rebuild-all": rebuild_all,
    }

# --- Main ------------------------------------------------------------------- #


def missing_command(command):
    print(BRIGHT_RED + "ERROR: " + RESET + "No action named '%s'!" % command)
    print(BRIGHT_WHITE + "See: " + RESET + "./tools help.")


def main(argc, argv):

    targets = list_targets("sources")

    if (argc >= 2):
        action = argv[1]

        if action in actions:
            if argc < 3:
                print(BRIGHT_RED + "ERROR: " + RESET + "No target specified!")
            else:
                target = argv[2]

                if target in targets:
                    actions[action](targets[target], targets)
                else:
                    print(BRIGHT_RED + "ERROR: " + RESET +
                          "No target named '%s'!" % target)

        elif action in global_actions:
            global_actions[action](targets)

        else:
            missing_command(action)
    else:
        help_command(targets)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)