"""
Taxonomy for Time-Domain Astronomy Classes

The taxonomy is captured in the file `tdtax/tdclass.yaml`
and is validated against the schema file `tdtax/schema.json`
"""
import json

import yaml
from yaml import Loader

taxonomy = yaml.load(open("tdtax/tdclass.yaml"), Loader=Loader)
schema = json.load(open("tdtax/schema.json", "r"))

__all__ = ["taxonomy", "schema"]

__version__ = '0.0.1'
