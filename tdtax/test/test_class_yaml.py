import json
import glob

import pytest

from jsonschema import validate
from jsonschema.exceptions import ValidationError

import yaml
from yaml import Loader


def test_schema():
    # this should not raise an exception, as it should be
    # be valid json
    _ = json.load(open("tdtax/schema.json", "r"))


def test_top():

    # check out the top.yaml file
    instance = yaml.load(open("tdtax/top.yaml"), Loader=Loader)
    schema = json.load(open("tdtax/schema.json", "r"))

    validate(instance=instance, schema=schema)


def test_all_yamls():

    schema = json.load(open("tdtax/schema.json", "r"))

    for f in glob.glob("tdtax/*.yaml"):
        instance = yaml.load(open(f, "r"), Loader=Loader)
        validate(instance=instance, schema=schema)


def test_bad_yaml():
    """
    this yaml should fail against the schema
    """
    schema = json.load(open("tdtax/schema.json", "r"))

    instance = yaml.load(open("tdtax/test/bad.yaml", "r"), Loader=Loader)

    with pytest.raises(ValidationError):
        validate(instance=instance, schema=schema)
