Usage
#####

For an existing Sphinx documentation set, the Alice theme can be applied by
configuring the |html_theme|_ value to ``sphinx_alice_theme``. For example:

.. code-block:: python

    html_theme = 'sphinx_alice_theme'

For users who wish to test this theme against their documentation set without
modifying a configuration file, the following can be invoked for the ``html``
builder:

.. code-block:: shell-session

    $ sphinx-build -b html . _build/html -E -a -D html_theme=sphinx_alice_theme
       (or)
    $ python -m sphinx -b html . _build/html -E -a -D html_theme=sphinx_alice_theme

Or the following for the ``singlehtml`` builder:

.. code-block:: shell-session

    $ sphinx-build -b singlehtml . _build/singlehtml -E -a -D html_theme=sphinx_alice_theme
       (or)
    $ python -m sphinx -b singlehtml . _build/singlehtml -E -a -D html_theme=sphinx_alice_theme

.. |html_theme| replace:: ``html_theme``
.. _html_theme: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme
