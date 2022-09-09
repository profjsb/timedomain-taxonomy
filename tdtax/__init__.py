"""
Taxonomy for Time-Domain Astronomy Classes

The taxonomy is captured in the file `tdtax/tdclass.yaml`
and is validated against the schema file `tdtax/schema.json`
"""
import os
from os.path import join as pjoin
import json

import yaml
from yaml import Loader
from jsonschema import validate

from .util import write_viz, merge_yamls

_basedir = os.path.dirname(__file__)
schema = json.load(open(pjoin(_basedir, "schema.json"), "r"))

# get the taxonomy and validate - raise an error if this does
# not validate against the schema
taxonomy = merge_yamls(pjoin(_basedir, "top.yaml"))
validate(instance=taxonomy, schema=schema)

# get a version of the taxonomy suitable for vega/d3 viz
taxstr = json.dumps(taxonomy)
taxstr = taxstr.replace('"class":', '"name":') \
               .replace('"subclasses":', '"children":')
vega_taxonomy = json.loads(taxstr)

__version__ = '0.1.5'

__all__ = ["taxonomy", "schema", "vega_taxonomy", "write_viz", "__version__"]

del (taxstr, merge_yamls, os, json, yaml, Loader, pjoin)
