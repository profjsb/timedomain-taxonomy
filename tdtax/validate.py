#! /usr/bin/env python
"""
small command-line script to validate YAML files
against the schema
"""

import argparse
import json
import glob

from jsonschema import validate, ValidationError
import yaml
from yaml import Loader
from yaml.scanner import ScannerError

CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'
CBOLD = '\33[1m'


def is_valid(fname, schema):
    try:
        instance = yaml.load(open(fname), Loader=Loader)
        validate(instance=instance, schema=schema)
        ret = f"{fname} is " + CBOLD + CGREEN + "valid" + CEND
    except ScannerError:
        ret = CRED + f"{fname} is not valid YAML." + CEND
    except ValidationError:
        ret = CRED + f"{fname} is not against the schema." + CEND
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='validate YAML files')

    parser.add_argument('--schema', default='schema.json',
                        help="JSON file of the schema [default=schema.json]")
    parser.add_argument('yaml_files', nargs='*', default=glob.glob("*.yaml"),
                        help=(
                            "UNIX list/wildcard of the files to validate"
                            " [default=*.yaml]"
                            )
                        )

    args = parser.parse_args()

    schema = json.load(open(args.schema, "r"))

    for fname in args.yaml_files:
        print(is_valid(fname, schema))
