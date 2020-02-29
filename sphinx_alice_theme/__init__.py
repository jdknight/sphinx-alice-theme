# -*- coding: utf-8 -*-
# Copyright 2020 James Knight

from os import path

__version__ = '0.0.0-dev0'

def setup(app):
    app.add_html_theme('sphinx_alice_theme',
        path.abspath(path.dirname(__file__)))

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': __version__,
    }
