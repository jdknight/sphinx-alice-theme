# -*- coding: utf-8 -*-
# Copyright 2020-2021 James Knight

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
html_show_copyright = False

html_extra_path = [
    'assets/overview.png',  # deprecated
    'assets/overview-01.png',
    'assets/overview-02.png',
    'assets/overview-03.png',
    'assets/overview-04.png',
    'assets/overview-05.png',
    'assets/overview-06.png',
    'assets/overview-07.png',
    'assets/overview-08.png',
    'assets/overview-09.png',
    '.nojekyll',
    'CNAME',
]
