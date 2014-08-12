
# -*- coding: utf-8 -*-
#
# sampledoc documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 11 05:04:40 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
sys.path.insert(0, os.path.abspath('_ext'))
try:
    import sphinxcontrib.doxylink
except ImportError:
    
    print('Unable to import sphinxcontrib.doxylink; try to run "pip install sphinxcontrib-doxylink"')

#~ # If your extensions are in another directory, add it here. If the directory
#~ # is relative to the documentation root, use os.path.abspath to make it
#~ # absolute, like shown here.
#~ sys.path.append(os.path.abspath('sphinxext'))

doxylink = {
    'cpapi' : ('../CoolPropDoxyLink.tag', 'http://www.coolprop.dreamhosters.com/doc/CoolProp5/')
}    

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autodoc',
              'sphinx.ext.mathjax',
              'sphinx.ext.extlinks',
              'sphinxcontrib.napoleon',
              'sphinxcontrib.doxylink',
              'matplotlib.sphinxext.plot_directive',
              'edit_on_github',  # see https://gist.github.com/mgedmin/6052926#file-edit_on_github-pyb
              
              # cloud's extensions
            #'cloud_sptheme.ext.autodoc_sections',
            #'cloud_sptheme.ext.index_styling',
            'cloud_sptheme.ext.relbar_toc',
            #'cloud_sptheme.ext.escaped_samp_literals',
            #'cloud_sptheme.ext.issue_tracker',
            #'cloud_sptheme.ext.table_styling',
              
              #'inheritance_diagram',
              #'numpydoc',
              #'breathe'
              ]

plot_formats = [('png',80)]

index_doc = "index"

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'CoolProp'
copyright = u'2012, Ian Bell'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
import CoolProp
ver = CoolProp.__version__
# The short X.Y version.
version = ver.rsplit('.',1)[0]
# The full version, including alpha/beta/rc tags.
release = ver

extlinks = {'sfdownloads': ('http://sourceforge.net/projects/coolprop/files/CoolProp/'+release+'/%s',''),
            'bbbinaries': ('http://www.coolprop.dreamhosters.com:8010/binaries/%s','')}

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build','sphinxext']

# The reST default role (used for this markup: `text`) to use for all documents.
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

#This value selects what content will be inserted into the main body of an autoclass directive.
#'class' - Only the class’ docstring is inserted. This is the default.
#'init' - Only the __init__ method’s docstring is inserted.
#'both' - Both the class’ and the __init__ method’s docstring are concatenated and inserted
autoclass_content = 'both' 


# -- Options for HTML output ---------------------------------------------------

try:
    import cloud_sptheme as csp
except:
    print('unable to import cloud_sptheme as csp; try a "pip install cloud_sptheme"')
    
# import Cloud
import cloud_sptheme as csp

# ... some contents omitted ...

# set the html theme
html_theme = "cloud"
    # NOTE: there is also a red-colored version named "redcloud"

# ... some contents omitted ...

# set the theme path to point to cloud's theme data
html_theme_path = [csp.get_theme_dir()]

# [optional] set some of the options listed above...
html_theme_options = { "roottarget": "index",
                       "max_width" : "13in",
                       "logotarget": "index"
                       }

edit_on_github_project = 'CoolProp/CoolProp'
edit_on_github_branch = 'master'
edit_on_github_path_prefix = 'Web'

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
## html_theme = 'sphinxdoc'

## html_theme='nature'

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'Coolprop.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/PVTCP.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Content template for the index page.
#html_index = 'index.html'

# Custom sidebar templates, maps page names to templates.
# html_sidebars = {'index': 'indexsidebar.html',
#                  }

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'sampledocdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('contents', 'CoolPropdoc.tex', u'CoolProp Documentation',
   u'Ian Bell', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
