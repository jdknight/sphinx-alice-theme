# -*- coding: utf-8 -*-
# Copyright 2020 James Knight

from docutils import nodes
from os import path
from sphinx.transforms.post_transforms import SphinxPostTransform

__version__ = '0.1.0-dev0'

class AliceThemeTransform(SphinxPostTransform):
    default_priority = 400

    def run(self, **kwargs):
        for node in self.document.traverse(nodes.reference):
            # tag references with `inline` child with a `inline-link` class
            # (to style citation references)
            if isinstance(next(iter(node.children), None), nodes.inline):
                classes = node.get('classes', [])
                classes.append('inline-link')
            # tag references with `literal` child with a `literal-link` class
            # (to suppress hover styling)
            elif isinstance(next(iter(node.children), None), nodes.literal):
                classes = node.get('classes', [])
                classes.append('literal-link')

def setup(app):
    app.add_html_theme('sphinx_alice_theme',
        path.abspath(path.dirname(__file__)))
    app.add_post_transform(AliceThemeTransform)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': __version__,
    }
