# Time-domain Astronomy Taxonomy

[![Build Status](https://travis-ci.org/profjsb/timedomain-taxonomy.svg?branch=master)](https://travis-ci.org/profjsb/timedomain-taxonomy)

This project helps us track and version a taxonomy for astronomical time-series sources, for transients (e.g., supernovae and tidal-distruption events), continuous variables (e.g., QSOs) and variable stars (RR Lyrae, &delta;-Scuti). It is open source and we welcome PRs to change/update this taxonomy as need be.

The generic structure is human-readable YAML and looks like:

```
Time-domain Source:
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
Only the `class` name is required at each level. Other keys (`subclasses`, `comments`, `tags`, `other names`, and `links`) are allowed but not required. The schema is created such that the classification hierarchy is nested: each member of the `subclasses` array is itself a `class`. The idea of `tags` to is to allow for a query of different `class` members throughout the taxonomy by a similar observation or physical inference (e.g., a search on `cosmology` could return both `Ia` and `IIP` supernovae).
 
## Installation

```
git clone https://github.com/profjsb/timedomain-taxonomy.git
cd timedomain-taxonomy
pip install .
```

## Usage

To get the taxonomy, after installation, as a Python `dict`:

```
from tdtax import taxonomy
```

## Contributing

The taxonomy is captured in the file `tdtax/tdclass.yaml`
and is validated against the schema file `tdtax/schema.json`. Before a PR, test to make sure that  taxonomy validates against the schema by running the tests:

```
pytest
```

This uses `PyYAML` to validate the taxonomy against the schema. When you make a PR, your branch will be automatically be tested with Travis CI.