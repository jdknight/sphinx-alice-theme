# -*- coding: utf-8 -*-
# Copyright 2020 James Knight

import os
import sys

# inject theme path into sphinx's registry (for git-repository builds)
doc_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(doc_dir)
sys.path.insert(0, root_dir)

# common
master_doc = 'index'

# meta
project = 'Alice Theme for Sphinx'
copyright = '2020 James Knight'
author = 'James Knight'

# sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_alice_theme',
]

# output - html
html_theme = 'sphinx_alice_theme'
html_theme_path = ['../']
html_theme_options = {
    'navigation_depth': 2,
}
html_extra_path = [
    'assets/overview.png',
    '.nojekyll',
    'CNAME',
]
