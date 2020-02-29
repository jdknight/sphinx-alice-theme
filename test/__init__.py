# -*- coding: utf-8 -*-
# Copyright 2020 James Knight

from os import environ
from os import path
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace
import shutil
import sys
import unittest

class TestAliceTheme(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_dir = path.dirname(path.realpath(__file__))
        self.root_dir = path.dirname(self.test_dir)
        self.doc_dir = path.join(self.root_dir, 'Documentation')

    def test_html_builder(self):
        out_dir, doctree_dir = self._prepare_output('html')
        self._build_documentation('html', out_dir, doctree_dir)

    def test_singlehtml_builder(self):
        out_dir, doctree_dir = self._prepare_output('singlehtml')
        self._build_documentation('singlehtml', out_dir, doctree_dir)

    def _prepare_output(self, name):
        prefix = ''
        if 'TOX_ENV_NAME' in environ:
            prefix = environ['TOX_ENV_NAME'] + '-'

        output_dir = path.join(self.test_dir, '_build')
        container_dir = path.join(output_dir, prefix + name)
        out_dir = path.join(container_dir, 'build')
        doctree_dir = path.join(container_dir, 'doctree')

        shutil.rmtree(container_dir, ignore_errors=True)
        return out_dir, doctree_dir

    def _build_documentation(self, builder, out_dir, doctree_dir, config=None):
        conf = dict(config) if config else {}
        conf['master_doc'] = 'index' # force index for legacy sphinx
        conf['html_theme'] = 'sphinx_alice_theme'
        conf['html_theme_path'] = self.root_dir

        with docutils_namespace():
            app = Sphinx(
                self.doc_dir,        # documentation to process
                None,                # default configuration
                out_dir,             # output for generated documents
                doctree_dir,         # output for doctree files
                builder,             # builder to execute
                confoverrides=conf,  # load provided configuration (volatile)
                warning=sys.stderr,  # warnings output
                warningiserror=True) # treat warnings as errors

            app.build(force_all=True)
