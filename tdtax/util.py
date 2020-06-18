import os
import json
import pkgutil
import datetime
import ast

import yaml
from yaml import Loader

# Get version without importing module
mod = ast.parse(pkgutil.get_data(__name__, "__init__.py").decode())
assignments = [node for node in mod.body if isinstance(node, ast.Assign)]
__version__ = [node.value.s for node in assignments
               if node.targets[0].id == '__version__'][0]


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
