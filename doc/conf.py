# Configuration file for the Sphinx documentation builder.

from docutils import nodes
from docutils.parsers.rst import roles

def greyed_out_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, classes=["greyed-out"])
    return [node], []

roles.register_local_role('grey', greyed_out_role)

# -- Project information

project = 'Climate-Space-405'
copyright = '2024, CLASP'
author = 'Cheng Li'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Custom options
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]
