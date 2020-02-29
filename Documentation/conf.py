# -*- coding: utf-8 -*-
# Copyright 2020 James Knight

# common
master_doc = 'index'

# meta
project = 'Alice Theme for Sphinx'
copyright = '2020 James Knight'
author = 'James Knight'

# sphinx extensions
extensions = [
]

# output - html
html_theme = 'sphinx_alice_theme'
html_theme_path = ['../']
html_theme_options = {
    'navigation_depth': 2,
}
html_extra_path = [
    '.nojekyll',
    'CNAME',
]
