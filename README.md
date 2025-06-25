# doorstop-to-mermaid

**Generate [mermaid](https://mermaid.js.org/) diagram source from a [doorstop](https://doorstop.readthedocs.io/) requirements document.**

[![CI Status](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/ci.yml/badge.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/ci.yml)
[![Wheel Status](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/wheels.yml/badge.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/wheels.yml)
[![Security check - Bandit](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/bandit.yml/badge.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/bandit.yml)
[![Release Status](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/release.yml/badge.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/release.yml)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Test coverage](https://raw.githubusercontent.com/sarnold/doorstop-to-mermaid/badges/main/test-coverage.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/coverage.yml)
[![Pylint Score](https://raw.githubusercontent.com/sarnold/doorstop-to-mermaid/badges/main/pylint-score.svg)](https://github.com/sarnold/doorstop-to-mermaid/actions/workflows/pylint.yml)

[![GitHub tag](https://img.shields.io/github/v/tag/sarnold/doorstop-to-mermaid?color=green&include_prereleases&label=latest%20release)](https://github.com/sarnold/doorstop-to-mermaid/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/sarnold/doorstop-to-mermaid/blob/main/LICENSE)
[![REUSE status](https://api.reuse.software/badge/git.fsfe.org/reuse/api)](https://api.reuse.software/info/git.fsfe.org/reuse/api)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## What is doorstop?

Doorstop uses git to manage project-specific data, where each linkable
item (requirement, test case, etc.) is stored as either a YAML or
Markdown file in a designated (sub)directory.

The items in each directory form a document. The relationship between
documents forms a tree hierarchy. Doorstop provides mechanisms for
modifying this tree, validating item traceability, and publishing
documents in several formats.

## What is mermaid?

Mermaid is a diagramming and charting tool with (partial) Github
rendering support anywhere Markdown is used, including `anything.md`
files, issues, and pull requests.

Markdown is already a common way to present useful information with rich
formatting from a relatively simple human readable syntax. Especially
useful is being able to highlight code blocks for mermaid.

Mermaid-JS takes this philosophy and applies it to graphs, taking simple
human-readable syntax and returning rich graphs.

See the [unofficial example gist](https://gist.github.com/ChristopherA/bffddfdf7b1502215e44cec9fb766dfd)
for example diagram ideas.

## Quick start

ds2mermaid is currently a small Python helper module for generating a
mermaid diagram using subgraphs. The primary use case for subgraphs is
to represent a set of doorstop documents, where each subgraph contains
the nodes for a single document. Any links found in child docments are
represented as mermaid edges from child to parent node.

The package provides an example script to generate a diagram from the
discovered document prefixes, item UIDs, and links.

Therefor, the 2 ways to consume the ds2mermaid package are:

* build and install the package and run the example script
* add the package to your project dependencies and import the bits you need

The current example script supports *very* minimal command options and
there are no required arguments:

    (dev) user@host $ gendiagram.py -h
    usage: gendiagram.py [-h] [--version] [-v]

    Example calling script for ds2mermaid

    options:
      -h, --help     show this help message and exit
      --version      show program's version number and exit
      -v, --verbose  display more logging info (default: False)

Enabling the verbose option *will* pollute the top of the graph with
a line of debug output. The script simply echoes the mermaid source
to `stdout` which you can redirect to a file.

### Caveats

Mermaid on Github ignores any elk comments so Github rendering is limited
to the default renderer, which is less than optimal.

### Prerequisites

Creating a useful diagram with the example script depends entirely on
existing doorstop document data, ie, at least one document is required
for the subgraph feature. The effective minimum for a *useful* diagram
however, is a parent document *with at least one* child document that
includes links to the parent.

### Install with pip

This package is *not* yet published on PyPI, thus use one of the following
to install ds2mermaid on any platform. Install from the main branch using:

    pip install git+https://github.com/sarnold/doorstop-to-mermaid.git@main

or use this command to install a specific release version:

    pip install git+https://github.com/sarnold/doorstop-to-mermaid.git@0.1.0

The full package provides the `ds2mermaid` module as well as a working
example calling script.

If you'd rather work from the source repository, it supports the common
idiom to install it on your system in a virtual env after cloning:

    python -m venv env
    source env/bin/activate
    (env) $ pip install .
    (env) $ gendiagram.py --version
    gendiagram.py 0.0.1.dev36+gd33fdf7
    (env) $ deactivate

The alternative to python venv is the Tox_ test driver shown below.

## Contributing

Local tool dependencies to aid in development; install them for maximum
enjoyment.

### Tox

As long as you have git and at least Python 3.8, then you can install
and use [tox](https://github.com/tox-dev/tox). After cloning the
repository, you can run the repo checks with the `tox` command. It will
build a virtual python environment for each installed version of python
with all the python dependencies and run the specified commands, eg:

    git clone https://github.com/sarnold/doorstop-to-mermaid
    cd doorstop-to-mermaid/
    tox -e py

The above will run the default test command using the (local) default
Python version. To specify the Python version and host OS type, run
something like:

    tox -e py311-linux

To build and check the Python package, run:

    tox -e build,check

Full list of additional `tox` commands:

* `tox -e dev` build a python venv and install in editable mode
* `tox -e build` build the python packages and run package checks
* `tox -e check` install the wheel package from above
* `tox -e lint` run `pylint` (somewhat less permissive than PEP8/flake8
  checks)
* `tox -e mypy` run mypy import and type checking
* `tox -e style` run flake8 style checks
* `tox -e reuse` run the `reuse lint` command and install sbom4python
* `tox -e changes` generate a new changelog file

To build/lint the api docs, use the following tox commands:

* `tox -e docs` build the documentation using sphinx and the api-doc
  plugin
* `tox -e ldocs` run the Sphinx doc-link checking
* `tox -e cdocs` run `make clean` in the docs build

We use [gitchangelog](https://github.com/sarnold/gitchangelog) to
generate a changelog and/or release notes, as well as the gitchangelog
message format to help it categorize/filter commits for tidier output.
Please use the appropriate ACTION modifiers for important changes in
Pull Requests.

### Pre-commit

This repo is also [pre-commit](http://pre-commit.com/) enabled for
various linting and format checks. The checks run automatically on
commit and will fail the commit (if not clean) with some checks
performing simple file corrections.

If other checks fail on commit, the failure display should explain the
error types and line numbers. Note you must fix any fatal errors for the
commit to succeed; some errors should be fixed automatically (use
`git status` and `git diff` to review any changes).

See the following sections for more information on gitchangelog and
pre-commit.

You will need to install pre-commit before contributing any changes;
installing it using your system's package manager is recommended,
otherwise install with pip into your usual virtual environment using
something like:

    sudo emerge pre-commit  # --or--
    pip install pre-commit

then install it into the repo you just cloned:

    git clone git@github.com:sarnold/doorstop-to-mermaid.git
    cd doorstop-to-mermaid/
    pre-commit install --install-hooks

It's usually a good idea to update the hooks to the latest version:

    pre-commit autoupdate

## SBOM and license info

This project is now compliant with the REUSE Specification Version 3.3,
so the corresponding license information for all files can be found in
the `REUSE.toml` configuration file with license text(s) in the
`LICENSES/` folder.

Related metadata can be (re)generated with the following tools and
command examples.

* [reuse-tool](https://github.com/fsfe/reuse-tool) -
  [REUSE](https://reuse.software/spec-3.3/) compliance linting and sdist
  (source files) SBOM generation
* [sbom4python](https://github.com/anthonyharrison/sbom4python) -
  generate SBOM with full dependency chain

### Commands

Use tox to create the environment and run the lint command:

    tox -e reuse                      # --or--
    tox -e reuse -- spdx > sbom.txt   # generate sdist files sbom

Note you can pass any of the other reuse commands after the `--` above.

Use the above environment to generate the full SBOM in text format:

    source .tox/reuse/bin/activate
    sbom4python --system --use-pip -o <file_name>.txt

Be patient; the last command above may take several minutes. See the doc
links above for more detailed information on the tools and
specifications.
