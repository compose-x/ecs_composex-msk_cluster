#!/usr/bin/env python

import sphinx_material

try:
    import ecs_composex_msk_cluster
except ImportError:
    import os
    import sys

    sys.path.insert(0, os.path.abspath('..'))
    import ecs_composex_msk_cluster


extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

master_doc = 'index'
project = 'ecs_composex_msk_cluster'
copyright = '2022, John "Preston" Mille'
author = "John Preston"

version = ecs_composex_msk_cluster.__version__
release = ecs_composex_msk_cluster.__version__
language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

extensions += [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx-jsonschema",
    "sphinx_material"
]

autosummary_generate = True
autoclass_content = "class"

html_baseurl = "https://msk-cluster.docs.compose-x.io"

html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "Compose-X MSK Cluster",
    # 'google_analytics_account': 'UA-XXXXX',
    "base_url": "https://docs.msk-cluster.ecs-composex.io",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "color_primary": "blue-grey",
    "color_accent": "white",
    "repo_url": "https://github.com/compose-x/ecs_composex_msk_cluster/",
    "repo_name": "compose-x/ecs_composex_msk_cluster",
    "repo_type": "github",
    "globaltoc_depth": 2,
    "globaltoc_collapse": True,
    "globaltoc_includehidden": False,
}

html_static_path = ["_static"]
html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

htmlhelp_basename = 'ecs_composex_msk_clusterdoc'

latex_elements = {}
latex_documents = [
    (master_doc, 'ecs_composex_msk_cluster.tex',
     'msk_cluster Documentation',
     'John Preston', 'manual'),
]

man_pages = [
    (master_doc, 'ecs_composex_msk_cluster',
     'msk_cluster Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'ecs_composex_msk_cluster',
     'msk_cluster Documentation',
     author,
     'ecs_composex_msk_cluster',
     'One line description of project.',
     'Miscellaneous'),
]
