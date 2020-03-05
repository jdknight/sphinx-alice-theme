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
    'sphinx.ext.autodoc',
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

# inject theme into sphinx's registry (for git-repository builds)
def setup(app):
    app.registry.load_extension(app, 'sphinx_alice_theme')
