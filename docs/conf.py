# SPDX-License-Identifier: Apache-2.0
#
# SPDX-FileCopyrightText: © 2025 Tenstorrent AI ULC

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import collections

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("."))

SphinxConfig = collections.namedtuple("SphinxConfig", ["fullname", "shortname"])

sphinx_config = SphinxConfig(fullname="TT-NN Visualizer&trade;", shortname="ttnn_visualizer")

# -- Project information -----------------------------------------------------

project = sphinx_config.fullname
copyright = "2025, Tenstorrent"
author = "Tenstorrent"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinxcontrib.email",
    "sphinx.ext.mathjax",
    "sphinx_sitemap",
    "myst_parser",
]

sitemap_locales = [None]
sitemap_url_scheme = "{link}"

source_suffix = [".rst", ".md"]

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Email settings
email_automode = True

# Add any paths that contain templates here, relative to this directory.
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

import subprocess as _sp


def _git_tags():
    try:
        out = _sp.check_output(
            ["git", "tag", "-l", "v*", "--sort=-version:refname"],
            stderr=_sp.DEVNULL,
        ).decode().strip()
        return [t for t in out.split("\n") if t]
    except Exception:
        return []


_VISUALIZER_BASE = "https://firdovsimammedovk.github.io/tt-visualizer-sandbox/"
_GLOBAL_CSS = "https://firdovsimammedovk.github.io/tenstorrent-sandbox/_static/tt_theme.css"
_current_version = os.environ.get("DOCS_VERSION", "latest")

_all_versions = ["latest"] + [t for t in _git_tags() if t != "latest"]
_version_urls = [(v, f"{_VISUALIZER_BASE}{v}/") for v in _all_versions]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,
    "titles_only": True,
    "navigation_depth": 2,
}
html_logo = "shared/images/tt_logo.svg"
html_favicon = "shared/images/favicon.png"
html_static_path = ["shared/_static"]
html_extra_path = []
templates_path = ["shared/_templates"]
html_last_updated_fmt = "%b %d, %Y"

html_baseurl = f"{_VISUALIZER_BASE}{_current_version}/"
version = _current_version

# Load global CSS from tenstorrent-sandbox CDN; local tt_theme.css adds overrides
html_css_files = [_GLOBAL_CSS]

html_context = {
    "versions": _version_urls,
    "current_version": _current_version,
    "logo_link_url": "https://firdovsimammedovk.github.io/tenstorrent-sandbox/",
}


def setup(app):
    app.add_css_file("tt_theme.css")
