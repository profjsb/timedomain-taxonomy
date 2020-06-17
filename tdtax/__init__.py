"""
Taxonomy for Time-Domain Astronomy Classes

The taxonomy is captured in the file `tdtax/tdclass.yaml`
and is validated against the schema file `tdtax/schema.json`
"""
import os
from os.path import join as pjoin
import json
import pkgutil
import datetime

import yaml
from yaml import Loader
from jsonschema import validate


_basedir = os.path.dirname(__file__)
schema = json.load(open(pjoin(_basedir, "schema.json"), "r"))


def write_viz(vega_taxonomy, outname="viz.html"):
    """
    Use the current taxonomy to vizualize the tree
    with d3.

    >> import tdtax
    >> tdtax.write_viz(tdtax.vega_taxonomy)

    """
    text = pkgutil.get_data(__name__, "viz_template.html").decode()
    text = text.replace("%%JSON%%", json.dumps(vega_taxonomy))
    text = text.replace("%%VERSION%%", __version__)
    text = text.replace("%%DATE%%", str(datetime.datetime.utcnow()))
    f = open(outname, "w")
    f.write(text)
    f.close()
    print(f"wrote {outname}")


def walk_and_replace(d, path="./", verbose=False):
    """
    recursively replace references to YAMLs
    """
    if not isinstance(d, dict):
        return

    for key, value in d.items():
        if isinstance(value, dict):
            walk_and_replace(value, path=path, verbose=verbose)
        elif isinstance(value, list):
            for i in range(len(value)):
                if isinstance(value[i], dict):
                    if value[i].get("ref") is not None:
                        ref = path + value[i].get("ref")
                        if os.path.exists(ref):
                            replacement = yaml.load(open(ref), Loader=Loader)
                            value[i] = replacement
                        else:
                            if verbose:
                                print(
                                    f"Did not find file {ref}."
                                    "Adding placeholder."
                                     )
                            basename = os.path.basename(ref).split(".")[0]
                            value[i] = {"class": basename + "-placeholder"}
                    walk_and_replace(value[i], path=path, verbose=verbose)


def merge_yamls(fname):
    taxonomy = yaml.load(open(fname), Loader=Loader)
    path = os.path.dirname(fname) + "/"
    walk_and_replace(taxonomy, path)
    return taxonomy


# get the taxonomy and validate
taxonomy = merge_yamls(pjoin(_basedir, "top.yaml"))
validate(instance=taxonomy, schema=schema)

# get a version of the taxonomy suitable for vega/d3 viz
taxstr = json.dumps(taxonomy)
taxstr = taxstr.replace('"class":', '"name":') \
           .replace('"subclasses":', '"children":')
vega_taxonomy = json.loads(taxstr)


__all__ = ["taxonomy", "schema", "merge_yamls", "vega_taxonomy", "write_viz"]

__version__ = '0.0.2'
