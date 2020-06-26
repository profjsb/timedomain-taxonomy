# Time-domain Astronomy Taxonomy

[![Build Status](https://travis-ci.org/profjsb/timedomain-taxonomy.svg?branch=master)](https://travis-ci.org/profjsb/timedomain-taxonomy)

<img src="https://raw.githubusercontent.com/profjsb/timedomain-taxonomy/master/taxonomy-viz.gif">

This project helps us track and version a taxonomy for astronomical time-series sources, for transients (e.g., supernovae and tidal-disruption events), continuous variables (e.g., QSOs) and variable stars (RR Lyrae, &delta;-Scuti). It is open source and we welcome PRs to change/update this taxonomy as need be.

The generic structure is human-readable YAML and looks like:

```
  class: Supernova
  comments: |
      This is a diverse class of explosions related
      to the end-of-life of stars.
  links:
    - https://astrobites.org/2016/12/02/classifying-supernovae/
    - https://en.wikipedia.org/wiki/Supernova
  tags: [explosive, transient]
  other names: [SN, sn, sne, supernova, supernovae]
  subclasses:
  - class: Type I
    tags: [hydrogen poor]
    other names: [SN Type I]
    subclasses:
    - class: Ia
      tags: [white dwarf, cosmology, thermonuclear]
      other names: [Ia-p, SN Ia, SNIa, supernovae Ia, SNe Ia]
      subclasses:
      - class: Ia-pec
        tags: [peculiar]
        other names: [SN Ia-pec, SNIa-pec, Ia-p]
     ...
```
There are two ways to describe the class. Either refer to another YAML file:

```
- class: Stellar variable
    subclasses:
      - ref: cataclysmic.yaml
      - ref: eclipsing.yaml
      - ...
```
or define the classes outright:

```
  - class: Novae
    tags: [binary]
    subclasses:
      - class: Classical Nova
        other names: []
```

In this case only the `class` name is required at each level. Other keys (`subclasses`, `comments`, `tags`, `other names`, and `links`) are allowed but not required. The schema is created such that the classification hierarchy is nested: each member of the `subclasses` array is itself a `class`. The idea of `tags` is to allow for a query of different `class` members throughout the taxonomy by a similar observation or physical inference (e.g., a search on `cosmology` could return both `Ia` and `IIP` supernovae).
 
## Installation

Using pypi:

```
pip install -U tdtax
```

Or Directly from Github:

```
git clone https://github.com/profjsb/timedomain-taxonomy.git
cd timedomain-taxonomy
pip install .
```

## Usage

To get the taxonomy, after installation, as a Python `dict`:

```
import tdtax
from tdtax import taxonomy
```
This will merge all the YAML taxonomy files referred to in the `top.yaml` file and check to make sure that the taxonomy is validate against the schema.

To output the current taxonomy to a webpage that can be interactively traversed:

```
import tdtax
tdtax.write_viz(tdtax.vega_taxonomy, outname="viz.html")
```
This will write a file `viz.html` which can be viewed in your browser. The `tags` associated with each node is shown upon hover.

## Contributing

The taxonomy is captured starting the file `tdtax/top.yaml`. It refers to other YAML files which contain classification hierarchies for subclasses.

Upon `import tdtax` the taxonomies are merged into a single JSON tree and this is validated against the schema file `tdtax/schema.json`. Before a PR, test to make sure that taxonomy validates against the schema by running the tests:

```
pytest
```

This uses `PyYAML` to validate the taxonomy against the schema. When you make a PR, your branch will be automatically be tested with Travis CI.

## Links

To learn more about taxonomy of variable stars and explosive transients we suggest the following links:

   - ["Variable stars" from CSIRO Astronomy and Space Science](https://www.atnf.csiro.au/outreach/education/senior/astrophysics/variable_types.html?newwindow=true)
   - [Variability types from GCVS](http://www.sai.msu.su/gcvs/gcvs/vartype.htm?newwindow=true)
   - [Supernova classification (astrobites)](https://astrobites.org/2016/12/02/classifying-supernovae/) from A. Villar

## Acknowledgements


We thank the Gordon and Betty Moore Foundation for a [Software SkyPortal grant](https://www.moore.org/grant-detail?grantId=GBMF9122) which covered the cost of the development of this project.

<a href="https://www.moore.org/grant-detail?grantId=GBMF9122"><img width=200 src="https://www.moore.org/content/images/logo-light.png"> </a>