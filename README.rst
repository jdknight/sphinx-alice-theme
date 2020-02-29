Alice Theme for Sphinx
======================

.. image:: https://img.shields.io/pypi/v/sphinx-alice-theme.svg
    :target: https://pypi.python.org/pypi/sphinx-alice-theme
    :alt: pip Version

.. image:: https://github.com/jdknight/sphinx-alice-theme/workflows/build/badge.svg?branch=master
    :target: https://github.com/jdknight/sphinx-alice-theme/actions?query=workflow%3Abuild
    :alt: Build

.. image:: https://github.com/jdknight/sphinx-alice-theme/workflows/docs/badge.svg?branch=master
    :target: https://sphinx-alice-theme.jdknight.me/
    :alt: Documentation

Provides the Alice theme for Sphinx_ projects.

.. image:: https://sphinx-alice-theme.jdknight.me/overview.png
   :align: center
   :width: 500px

installation
------------

This theme can be installed using pip_:

.. code-block:: shell

    pip install sphinx-alice-theme
        (or)
    python -m pip install sphinx-alice-theme

usage
-----

For an existing Sphinx documentation set, the Alice theme can be applied by
configuring the |html_theme|_ value to ``sphinx_alice_theme``. For example:

.. code-block:: python

    html_theme = 'sphinx_alice_theme'

.. |html_theme| replace:: ``html_theme``
.. _Sphinx: https://www.sphinx-doc.org/
.. _html_theme: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme
.. _pip: https://pip.pypa.io/
