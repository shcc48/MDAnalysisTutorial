# -*- coding: utf-8 -*-
#
# MDAnalysis Tutorial documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 30 00:40:26 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_sitemap',
]

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# for sitemap with https://github.com/jdillard/sphinx-sitemap
site_url = "https://www.mdanalysis.org/MDAnalysisTutorial/"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MDAnalysis Tutorial'
copyright = u'2015-2017, Oliver Beckstein, Max Linke'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '2.0.0'
# The short X.Y version.
version = ".".join(release.split('.')[:2])

# The minimum required MDAnalysis version (because we use
# semantic versioning, all releases for a given version
# should work, too). See rst_epilog below for setting it up
# as a replacement value in reST.
MDAnalysis_version = '0.16.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# to include decorated objects like __init__
autoclass_content = 'both'

# Define additional substitutions (like |release|)
# http://sphinx-doc.org/config.html#confval-rst_epilog
rst_epilog = """
.. |MDAnalysis_version| replace:: {0}
""".format(MDAnalysis_version)

# number figures and code blocks with captions
numfig = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# styles/fonts to match http://mdanalysis.org (see public/css)
#
# /* MDAnalysis orange: #FF9200 */
# /* MDAnalysis gray: #808080 */
# /* MDAnalysis white: #FFFFFF */
# /* MDAnalysis black: #000000 */

color = {'orange': '#FF9200',
         'gray': '#808080',
         'white': '#FFFFFF',
         'black': '#000000',}

from collections import OrderedDict
extra_nav_links = OrderedDict()
extra_nav_links['MDAnalysis'] = 'http://mdanalysis.org'
extra_nav_links['docs'] = 'http://docs.mdanalysis.org'
extra_nav_links['wiki'] = 'http://wiki.mdanalysis.org'
extra_nav_links['user discussion group'] = 'http://users.mdanalysis.org'
extra_nav_links['GitHub'] = 'https://github.com/mdanalysis'
extra_nav_links['@mdanalysis'] = 'https://twitter.com/mdanalysis'

html_theme_options = {
    'logo' : "logos/mdanalysistutorial-logo-200x150.png",
    'github_user': 'MDAnalysis',
    'github_repo': 'mdanalysis',
    'github_button': False,
    # 'github_type': 'star',
    'github_banner': True,
    'show_related': True,
    'fixed_sidebar': False,
    'sidebar_includehidden': True,
    'sidebar_collapse': True,
    # style
    'link': color['orange'],
    'link_hover': color['orange'],
    'gray_1': color['gray'],
    'narrow_sidebar_bg': color['gray'],
    'narrow_sidebar_fg': color['white'],
    # typography
    'font_family': "'PT Sans', Helvetica, Arial, 'sans-serif'",
    'head_font_family': "",
    'code_font_family': "Menlo, Monaco, 'Courier New', monospace",
    'caption_font_size': "smaller",
    # external links
    'extra_nav_links': extra_nav_links,
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/logos/mdanalysis-logo.ico"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, maps document names to template names.
# alabaster sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'MDAnalysisTutorial.tex', u'MDAnalysis Tutorial Documentation',
   u'Oliver Beckstein, Max Linke', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'mdanalysistutorial', u'MDAnalysis Tutorial Documentation',
     [u'Oliver Beckstein', u'Max Linke'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'MDAnalysisTutorial', u'MDAnalysis Tutorial Documentation',
   u'Oliver Beckstein, Max Linke', 'MDAnalysisTutorial', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://docs.mdanalysis.org/': None,
                       'http://matplotlib.org': None,
                       'http://docs.scipy.org/doc/numpy/': None,
                       }
