import json
from jsonschema import validate
import yaml
from yaml import Loader


def test_schema():
    # this should not raise an exception, as it should be
    # be valid json
    _ = json.load(open("tdtax/schema.json", "r"))


def test_yaml():
    instance = yaml.load(open("tdtax/tdclass.yaml"), Loader=Loader)
    schema = json.load(open("tdtax/schema.json", "r"))

    validate(instance=instance, schema=schema)
